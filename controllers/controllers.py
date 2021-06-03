# -*- coding: utf-8 -*-
# from odoo import http


# class Daltest(http.Controller):
#     @http.route('/daltest/daltest/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/daltest/daltest/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('daltest.listing', {
#             'root': '/daltest/daltest',
#             'objects': http.request.env['daltest.daltest'].search([]),
#         })

#     @http.route('/daltest/daltest/objects/<model("daltest.daltest"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('daltest.object', {
#             'object': obj
#         })
