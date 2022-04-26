# -*- coding: utf-8 -*-

from odoo import fields, models, api


class LibraryCategory(models.Model):
    _name = 'library.category'
    _description = 'Library Category'

    name = fields.Char(string="Name", required=True)
    book_ids = fields.One2many("library.book", "category_id", string="Book")
    note = fields.Text(string="Note")

