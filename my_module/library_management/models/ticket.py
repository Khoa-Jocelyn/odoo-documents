# -*- coding: utf-8 -*-

from odoo import fields, models, api


class LibraryTicket(models.Model):
    _name = 'library.ticket'
    _description = 'Library Ticket'
    _rec_name = 'name'
    
    name = fields.Char(string="Ticket Code", required=True)
    
    
