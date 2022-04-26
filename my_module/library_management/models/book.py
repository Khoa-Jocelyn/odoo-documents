# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import UserError
from pickle import TRUE


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'sequence, title'
    _rec_name = 'title'
    title = fields.Char(string="Title",
                        required=True,
                        store=True)
    state = fields.Selection(string='Status',
                             selection=[('still', 'Still'),
                                        ('over', 'Over')],
                                        compute="_compute_quantity",
                                        store=True,
                                        readonly=False,
                                        default='still')
    author_id = fields.Many2one('library.author',
                                string='Author',
                                ondelete="restrict")
    # author_name = fields.Char(string="Author Name", related="author_id.name", readonly=False)
    category_id = fields.Many2one('library.category',
                                  string='Category',
                                  ondelete="set null")
    number_of_pages = fields.Integer(string="Number Of Pages")
    producer_id = fields.Many2one('library.producer',
                                  string="Producer",
                                  ondelete="set null")
    publishing_year = fields.Char(string="Publishing Year")
    quantity = fields.Integer(string='Quantity',
                            required=True,
                            group_operator='sum')
    image = fields.Binary(string="Image", attachment=True)
    
    note = fields.Html(string="Note", sanitize=True)
    sequence = fields.Integer(string='Sequence', default=1)
    res_model_id = fields.Many2one(
        'ir.model', 'Document Model',
        ondelete='cascade', required=True)
    res_model = fields.Char(
        'Related Document Model',
        related='res_model_id.model', compute_sudo=True, store=True, readonly=True)
    res_id = fields.Many2oneReference(string='Related Document ID', index=True, required=True, model_field='res_model')
    res_name = fields.Char(
        'Document Name', compute='_compute_res_name', compute_sudo=True, store=True,
        help="Display name of the related document.", readonly=True)
    
    @api.model_create_multi
    def create(self, vals_list):
        """Override default Odoo create function and extend."""
        for vals in vals_list:
            if vals.get('title'):
                vals["title"] = vals["title"].title()
        return models.Model.create(self, vals_list)
    
    @api.depends('res_model', 'res_id')
    def _compute_res_name(self):
        for activity in self:
            activity.res_name = activity.res_model and \
                self.env[activity.res_model].browse(activity.res_id)


class LibraryBookExtend(models.Model):
    _inherit = "library.book"
    
    currency_id = fields.Many2one('res.currency', string='Currency')
    price = fields.Monetary(string="Price", digist=(10, 3), currency_field='currency_id',
                         states={'still': [('invisible', False), ('readonly', False), ("required", True)],
                                'over': [('invisible', True), ('readonly', True), ("required", False)]})
    total_price = fields.Float(string="Total Price", digist=(10, 3),
                               compute="_compute_total_price", store=True,
                               states={'still': [('invisible', False), ('readonly', False)],
                                       'over': [('invisible', True), ('readonly', True)]})
    
    @api.model
    def create(self, values):
        """Override default Odoo create function and extend."""
        # self.ensure_one()
        # self.flush()
        if values.get('title'):
            values["title"] = values["title"].title()
        return super(LibraryBookExtend, self).create(values)
    
    def write(self, values):
        """Override default Odoo write function and extend."""
        if values.get('title'):
            values["title"] = values["title"].title()
        return super(LibraryBookExtend, self).write(values)
    
    def unlink(self):
        """Override default Odoo unlink function and extend."""
        return super(LibraryBookExtend, self).unlink()
    
    @api.depends('price', 'quantity')
    def _compute_total_price(self):
        for r in self:
            if r.quantity > 0:
                r.total_price = r.quantity * r.price
            else:
                r.quantity = 0
                r.total_price = 0
    
    @api.depends('quantity')
    def _compute_quantity(self):
        for r in self:
            if r.quantity > 0:
                r.state = "still"
            else:
                r.state = "over"

    @api.model
    def is_allowed_state(self, current_state, new_state):
        allowed_states = [('still', 'over'), ('over', 'still')]
        return (current_state, new_state) in allowed_states
    
    def change_book_state(self, state):
        for book in self:
            if book.is_allowed_state(book.state, state):
                book.state = state
            else:
                raise UserError(("Changing book status from %s to %s is not allowed.") % (book.state, state))

    def change_to_still(self):
        self.change_book_state("still")
        if self.quantity <= 0:
            raise UserError("Quantity must be a number greater than zero!")

    def change_to_over(self):
        self.change_book_state("over")
        self.quantity = 0
    
    def test_state_book(self):
        print("Context: ", self.env.su)
        if self.env.context.get('test_state') == "over":
            self.state = "over"
            self.quantity = 0
        elif self.env.context.get('test_state') == "still":
            self.state = "still"
            self.quantity = 10
            
