# -*- coding: utf-8 -*-

from odoo import fields, models, api


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string="Title", required=True)
    # state = fields.Selection(string='Status', selection=[('other', 'Other'),
    #                                                     ('male', 'Male'),
    #                                                     ('female', 'Female')],
    #                                                 default='other')
    author_id = fields.Many2one('library.author',
                                string='Author',
                                ondelete="restrict")
                                # states={'other': [('invisible', True), ('readonly', True)],
                                #         'male': [('invisible', False), ('readonly', True)],
                                #         'female': [('invisible', True), ('readonly', True)]})
    category_id = fields.Many2one('library.category', string='Category', ondelete="set null")
    number_of_pages = fields.Integer(string="Number Of Pages")
    producer_id = fields.Many2one('library.producer', string="Producer", ondelete="set null")
    publishing_year = fields.Char(string="Publishing Year")
    amount = fields.Char(string='Amount', required=True)
    image = fields.Binary(string="Image", attachment=True)
    note = fields.Text(string="Note")
