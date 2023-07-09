# -*- coding: utf-8 -*-
# from odoo import http


# class Kamena/myaddons(http.Controller):
#     @http.route('/kamena/myaddons/kamena/myaddons', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kamena/myaddons/kamena/myaddons/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kamena/myaddons.listing', {
#             'root': '/kamena/myaddons/kamena/myaddons',
#             'objects': http.request.env['kamena/myaddons.kamena/myaddons'].search([]),
#         })

#     @http.route('/kamena/myaddons/kamena/myaddons/objects/<model("kamena/myaddons.kamena/myaddons"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kamena/myaddons.object', {
#             'object': obj
#         })
