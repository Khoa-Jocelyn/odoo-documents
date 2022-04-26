# -*- coding: utf-8 -*-

from odoo import fields, models, api


class LibraryCustomer(models.Model):
    _name = "library.customer"
    _description = 'Library Customer'
    _rec_name = 'name'
    
    name = fields.Char(string="Name", required=True)
    dob = fields.Date(string="Birth Day")
    age = fields.Integer(string='Age') 
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ], required=True, default="other")
    address = fields.Char(string="Address", required=True)
    phone = fields.Char(string="Phone Number", required=True)
    image = fields.Binary(string="Image", attachment=True)
    note = fields.Text(string="Note")
    

