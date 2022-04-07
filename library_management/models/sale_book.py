from odoo import models, fields, api


class LibraryLoanBook(models.Model):
    _inherit = "library.book"
    _description = "The books are for sale only"

    price = fields.Integer(string="Price")
    is_sale = fields.Boolean(string="Is Sale", default=False)
    
