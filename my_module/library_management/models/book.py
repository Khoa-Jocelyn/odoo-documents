# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo import _
from odoo.exceptions import UserError


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book Model'
    _order = 'sequence, title'
    _rec_name = 'title'

    title = fields.Char(string="Title", required=True, store=True)
    author_id = fields.Many2one('library.author',
                                string='Author',
                                ondelete="restrict")
    category_id = fields.Many2one('library.category', string='Category', ondelete="set null")
    number_of_pages = fields.Integer(string="Number Of Pages")
    producer_id = fields.Many2one('library.producer', string="Producer", ondelete="set null")
    publishing_year = fields.Char(string="Publishing Year")
    amount = fields.Integer(string='Amount', required=True, group_operator='sum')
    image = fields.Binary(string="Image", attachment=True)
    state = fields.Selection(string='Status', selection=[('still', 'Still'),
                                                        ('over', 'Over')], default='still')
    note = fields.Text(string="Note")
    sequence = fields.Integer(string='Sequence', default=1)
    
    @api.model_create_multi
    def create(self, vals_list):
        """Override default Odoo create function and extend."""
        for vals in vals_list:
            if vals.get('title'):
                vals["title"] = vals["title"].title()
        return models.Model.create(self, vals_list)


class LibraryBookExtendOther(models.Model):
    _inherit = "library.book"

    price = fields.Integer(string="Price", digist=(10, 3))
    total_price = fields.Float(string="Total Price", digist=(10, 3), compute="_compute_total_price", store=True, group_operator='sum')
    
    @api.model
    def create(self, values):
        """Override default Odoo create function and extend."""
        # self.ensure_one()
        # self.flush()
        if values.get('title'):
            values["title"] = values["title"].title()
        return super(LibraryBookExtendOther, self).create(values)
    
    def write(self, values):
        """Override default Odoo write function and extend."""
        if values.get('title'):
            values["title"] = values["title"].title()
        return super(LibraryBookExtendOther, self).write(values)
    
    def unlink(self):
        """Override default Odoo unlink function and extend."""
        return super(LibraryBookExtendOther, self).unlink()
    
    @api.depends('price', 'amount')
    def _compute_total_price(self):
        for r in self:
            if r.amount > 0: 
                r.total_price = r.price * r.amount
            else:
                r.total_price = False
    
    @api.model
    def is_allowed_state(self, current_state, new_state):
        allowed_states = [('still', 'over'), ('over', 'still')]
        return (current_state, new_state) in allowed_states
    
    def change_book_state(self, state):
        for book in self:
            if book.is_allowed_state(book.state, state):
                book.state = state
            else:
                raise UserError(_("Changing book status from %s to %s is not allowed.") % (book.state, state))

    def change_to_still(self):
        self.change_book_state("still")
    
    def change_to_over(self):
        self.change_book_state("over")
        
        
        
