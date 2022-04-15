# -*- coding: utf-8 -*-
# from odoo import http


# class QlBenhvien(http.Controller):
#     @http.route('/hospital_managerment/hospital_managerment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_managerment/hospital_managerment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_managerment.listing', {
#             'root': '/hospital_managerment/hospital_managerment',
#             'objects': http.request.env['hospital_managerment.hospital_managerment'].search([]),
#         })

#     @http.route('/hospital_managerment/hospital_managerment/objects/<model("hospital_managerment.hospital_managerment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_managerment.object', {
#             'object': obj
#         })
