# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author Model'
    _rec_name = 'name'

    name = fields.Char(string="Name", required=True)
    dob = fields.Date(string="Birth Day")
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
            if r.dob == False:
                r.age = 0
            elif r.dob >= fields.Date.today():
                raise ValidationError("Error date of birth: %s" % r.dob)
            else:
                r.age = fields.Date.today().year - r.dob.year
    
    @api.onchange("dob")
    def _onchange_dob(self):
        for r in self:
            if r.dob == False:
                r.age = 0
            elif r.dob >= fields.Date.today():
                raise ValidationError("Error date of birth: %s" % r.dob)
            else:
                r.age = fields.Date.today().year - r.dob.year
    
    @api.constrains("dob")
    def constrains_dob(self):
        for r in self:
            if r.dob == False:
                r.age = 0
            elif r.dob >= fields.Date.today():
                raise ValidationError("Error date of birth: %s" % r.dob)
            else:
                r.age = fields.Date.today().year - r.dob.year
    
    _sql_constraints = [('name', 'unique(name)', "The name of author already exists!")]
    _sql_constraints = [('age', 'check(age > 0)', "Error date of birth")]
    
    @api.model
    def create(self, values):
        """Override default Odoo create function and extend."""
        if values.get('name'):
            values["name"] = values["name"].title()
        return super(LibraryAuthor, self).create(values)
    
    def write(self, values):
        """Override default Odoo write function and extend."""
        if values.get('name'):
            values["name"] = values["name"].title()
        return super(LibraryAuthor, self).write(values)
    
    def unlink(self):
        """Override default Odoo unlink function and extend."""
        return super(LibraryAuthor, self).unlink()
    
    # def name_get(self):
    #     result = []
    #     for r in self:
    #         name = r.name
    #         result.append((r.name))
    #     return result
    #
    # @api.model
    # def name_search(self, name, args=None, operator="ilike", limit=100):
    #     args = args or []
    #     domain = []
    #     if name:
    #         domain = [('name', operator, name)]
    #     docs = self.search(domain + args, limit=limit)
    #     return docs.name_get()
    

