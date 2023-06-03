# -*- coding: utf-8 -*-
# from odoo import http


# class Lomi(http.Controller):
#     @http.route('/lomi/lomi', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lomi/lomi/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lomi.listing', {
#             'root': '/lomi/lomi',
#             'objects': http.request.env['lomi.lomi'].search([]),
#         })

#     @http.route('/lomi/lomi/objects/<model("lomi.lomi"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lomi.object', {
#             'object': obj
#         })
