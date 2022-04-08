# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author Model'

    name = fields.Char(string="Name", required=True)
    dob = fields.Date(string="Birth Day")
    today_v = fields.Date(string="To Day").today()
    age = fields.Integer(string='Age', compute='_compute_age', store=True) 
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ], required=True, default="other")
    introduce = fields.Text(string='Introduce')
    image = fields.Binary(string="Image", attachment=True)
    book_id = fields.One2many('library.book', "author_id", string="Book")
    note = fields.Text(string="Note")
    
    @api.depends('dob')
    def _compute_age(self):
        for r in self:
            if r.dob >= fields.Date.today() and r.dob == False:
                raise ValidationError("Error date of birth: %s" % r.dob)
            else:
                r.age = fields.Date.today().year - r.dob.year
    
    @api.onchange("dob")
    def _onchange_dob(self):
        for r in self:
            if r.dob >= fields.Date.today() and r.dob == False:
                raise ValidationError("Error date of birth: %s" % r.dob)
            else:
                r.age = fields.Date.today().year - r.dob.year
    
    @api.constrains("dob")
    def constrains_dob(self):
        for r in self:
            if r.dob >= fields.Date.today() and r.dob == False:
                raise ValidationError("Error date of birth: %s" % r.dob)
            
    
    _sql_constraints = [('name', 'unique(name)', "The name of author already exists!")]
    _sql_constraints = [('age', 'check(age > 0)', "Error date of birth")]
            
            
            
            