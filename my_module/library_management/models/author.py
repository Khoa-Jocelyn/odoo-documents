# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'
    _rec_name = 'name'

    name = fields.Char(string="Name", required=True)
    dob = fields.Date(string="Birth Day")
    age = fields.Integer(string='Age', compute='_compute_age',inverse = "_set_note", store=False, readonly=False) 
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ], required=True, default="other")
    introduce = fields.Text(string='Introduce')
    image = fields.Binary(string="Image", attachment=True)
    book_ids = fields.One2many('library.book', "author_id", string="Book")
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
        # for r in self:
        existing_record = self.env['library.author'].search([])
        for  r in self:
            if existing_record.filtered(lambda a: a.name == r.name):
                raise ValidationError('The name of author already exists!')
    
    _sql_constraints = [('name', 'unique(name)', "The name of author already exists!"),
                        ('age', 'check(age > 0)', "Error date of birth")]
    
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
        if self.name == False:
            record = self.create({"name": name,
                                  "dob": "1999-09-14",
                                  "gender": "male"})
            return record.name_get()[0]
        else:
            raise ValidationError("The name of author already exists!")
            return False
    
    def test_filtered(self):
        books = self.env['library.book'].search([])
        ids_filtered = books.filtered("id")
        # ids_filtered = books.filtered(lambda book: book.state == "still" )
        record = []
        for r in ids_filtered:
            record.append(r.title)
        print("All Book Ids Filtered: ", record)
        return ids_filtered
    
    def test_mapped(self):
        books = self.env['library.book'].search([])
        names_mapped = books.mapped("title")
        # names_mapped = books.mapped(lambda book: '%s' % (book.title))
        print("All Book Names Mapped: ", names_mapped)
        return names_mapped

    def test_sorted(self):
        books = self.env['library.book'].search([])
        ids_sotred = books.sorted(key="id", reverse=True)
        print("All Book Ids Sorted: ", ids_sotred)
        return ids_sotred
    
    def test_read_group(self):
        group_result = self.env['library.book'].read_group(
            [('state', '=', 'still')],  # domain
            ['author_id'],  # field
            ['author_id'])  # group by
        print("Read Group: ", group_result)
        return group_result

    def action_state_over(self):
        for r in self:
            context = self.env.context.copy()
            context.update({'test_state': "over"})
            r.book_ids.with_context(context).test_state_book()
            # r.book_ids.with_context({'test_state': "over"}).test_state_book()
        self.write({'note': "Change state to over"})
    
    def action_state_still(self):
        for r in self:
            # context = self.env.context.copy()
            # context.update({'test_state': "still"})
            # r.book_ids.with_context(context).test_archive_book()
            r.book_ids.with_context({'test_state': "still"}).test_state_book()
        self.write({'note': "Change state to still"})
        
    def _set_note(self):
        for r in self:
            if r.dob:
                r.note = str(r.dob)
