# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author Model'
    _rec_name = 'name'

    name = fields.Char(string="Name", required=True)
    dob = fields.Date(string="Birth Day")
    age = fields.Integer(string='Age', compute='_compute_age', store=True, readonly=False) 
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
        if self.dob == False:
            self.age = 0
        elif self.dob >= fields.Date.today():
            raise ValidationError("Error date of birth: %s" % self.dob)
        else:
            self.age = fields.Date.today().year - self.dob.year
    
    @api.constrains("dob")
    def constrains_check_dob(self):
        for r in self:
            if r.dob == False:
                r.age = 0
            elif r.dob >= fields.Date.today():
                raise ValidationError("Error date of birth: %s" % r.dob)
            else:
                r.age = fields.Date.today().year - r.dob.year
    
    @api.constrains('name')
    def constrains_check_name(self):
        for r in self:
            existing_record = self.env['library.author'].search_count([('name', '=', r.name)])
            if existing_record > 1:
                raise ValidationError('The name of author already exists!')
    
    # _sql_constraints = [('name', 'unique(name)', "The name of author already exists!"),
    #                     ('age', 'check(age > 0)', "Error date of birth")]
    
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
    
    def name_get(self):
        res = []
        for author in self:
            str = "Author: " + author.name 
            res.append((author.id, str))
        return res
    
    @api.model
    def name_search(self, name, args=None, operator="ilike", limit=100):
        args = args or []
        domain = []
        if name:
            domain = [('name', operator, name)]
        docs = self.search(domain + args, limit=limit)
        return docs.name_get()
    
    @api.model
    def name_create(self, name):
        return models.Model.name_create(self, name)
    
    def get_all_book_ids(self):
        books = self.env['library.book'].search([])
        ids_filtered = books.filtered("id")
        # ids_filtered = books.filtered(lambda book: book.id)
        print("All Book Ids Filtered: ", ids_filtered)
        return ids_filtered
    
    def get_all_book_names(self):
        books = self.env['library.book'].search([])
        names_mapped = books.mapped("title")
        # names_mapped = books.mapped(lambda c: c.title)
        print("All Book Names Mapped: ", names_mapped)
        return names_mapped

    def sort_book_ids(self):
        books = self.env['library.book'].search([])
        ids_sotred = books.sorted(key="id", reverse=True)
        print("All Book Ids Sorted: ", ids_sotred)
        return ids_sotred
    
    def group_by_author(self):
        group_result = self.env['library.book'].read_group(
            [('state', '=', 'still')], # domain
            ['author_id'], # field
            ['author_id']) # group by
        print("Read Group: ", group_result)
        return group_result