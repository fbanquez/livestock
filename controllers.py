# -*- coding: utf-8 -*-
from openerp import http

# class Livestock(http.Controller):
#     @http.route('/livestock/livestock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/livestock/livestock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('livestock.listing', {
#             'root': '/livestock/livestock',
#             'objects': http.request.env['livestock.livestock'].search([]),
#         })

#     @http.route('/livestock/livestock/objects/<model("livestock.livestock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('livestock.object', {
#             'object': obj
#         })