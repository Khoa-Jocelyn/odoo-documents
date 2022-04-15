# -*- coding: utf-8 -*-

from odoo import fields, models, api


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string="Title", required=True, store=True)
    # state = fields.Selection(string='Status', selection=[('other', 'Other'),
    #                                                     ('male', 'Male'),
    #                                                     ('female', 'Female')],
    #                                                 default='other')s
    author_id = fields.Many2one('library.author',
                                string='Author',
                                ondelete="restrict")
    category_id = fields.Many2one('library.category', string='Category', ondelete="set null")
    number_of_pages = fields.Integer(string="Number Of Pages")
    producer_id = fields.Many2one('library.producer', string="Producer", ondelete="set null")
    publishing_year = fields.Char(string="Publishing Year")
    amount = fields.Integer(string='Amount', required=True)
    image = fields.Binary(string="Image", attachment=True)
    note = fields.Text(string="Note")
    
    @api.model_create_multi
    def create(self, vals_list):
        print(vals_list)
        return models.Model.create(self, vals_list)
    
    
class LibraryLoanBook(models.Model):
    _inherit = 'library.book'
    
    is_borrow = fields.Boolean(string="Is Borrow", default=True)


class LibrarySaleBook(models.Model):
    _inherit = "library.book"

    price = fields.Integer(string="Price")
    is_sale = fields.Boolean(string="Is Sale", default=False)

