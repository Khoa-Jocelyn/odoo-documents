# -*- coding: utf-8 -*-
from odoo import api, fields, models


class BookWinzad(models.TransientModel):
    _name = "library.book.winzad"
    _description = "Library Book Winzad Model"
    
    author_id = fields.Many2one('library.author', string='Author', default=False)
    def multi_update_author_id(self):
        print(self.env.context)
        books = self.env["library.book"].browse(self.env.context['active_ids'])
        new_data = {}
        if self.author_id:
            new_data["author_id"] = self.author_id
        books.write(new_data)        
    
    
