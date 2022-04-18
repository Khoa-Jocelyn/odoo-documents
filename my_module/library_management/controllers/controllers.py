from odoo import http
from odoo.http import request


class Library(http.Controller):

    @http.route('/library/books', auth="public")
    def index(self, **kw):
        Books = http.request.env['library.book'].search([])
        return http.request.render('library_management.books', {
                'books':Books
            })
    
