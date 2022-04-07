# -*- coding: utf-8 -*-

from odoo import fields, models, api


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author Model'

    name = fields.Char(string="Name", required=True)
    dob = fields.Date(string="Birth Day")
    age = fields.Integer(string='Age', compute='_compute_age') 
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ], required=True, default="other")
    introduce = fields.Text(string='Introduce')
    image = fields.Binary(string="Image", attachment=True)
    book_id = fields.One2many('library.book', "author_id", string="Book")
    note = fields.Text(string="Note")
    
    # @api.depends('dob')
    def _compute_age(self):
        for r in self:
            if r.dob == False:
                r.age = 0
            else:
                r.age = fields.Date.today().year - r.dob.year
    

