# -*- coding: utf-8 -*-

from odoo import fields, models, api


class LibraryCategory(models.Model):
    _name = 'library.producer'
    _description = 'Library Producer Model'

    name = fields.Char(string="Name", required=True)
    infor = fields.Text(string="Information")
    book_id = fields.One2many("library.book", "producer_id", string="Book")
    note = fields.Text(string="Note")
