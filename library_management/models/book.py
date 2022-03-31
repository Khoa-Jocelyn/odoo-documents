# -*- coding: utf-8 -*-

from odoo import fields, models, api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string="Title", required=True)
    author_id = fields.Many2one('library.author', string='Author', required=True)
    category_id = fields.Many2one('library.category', string='Category', required=True)
    number_of_pages = fields.Integer(string="Number Of Pages")
    producer_id = fields.Many2one('library.producer', string="Producer", required=True)
    publishing_year = fields.Char(string="Publishing Year")
    amount = fields.Char(string='Amount', required=True)
    image = fields.Binary(string="Image", attachment=True)
    note = fields.Text(string="Note")
