from odoo import models, fields, api


class LibraryLoanBook(models.Model):
    _inherit = 'library.book'
    _description = 'The books are for sale only'
    
    is_borrow = fields.Boolean(string="Is Borrow", default=True)
    
