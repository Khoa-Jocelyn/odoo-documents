# -*- coding: utf-8 -*-

from odoo import fields, models, api

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char(string="Name", required=True)
    day_of_birth = fields.Date(sring="Day Of Birth")
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ], required=True, default="other")
    introduce = fields.Text(string='Introduce')
    image = fields.Binary(string="Image", attachment=True)
    book_id = fields.One2many('library.book', "author_id", string="Book")
    note = fields.Text(string="Note")
