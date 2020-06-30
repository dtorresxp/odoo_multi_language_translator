# -*- coding: utf-8 -*-
# from odoo import http


# class GoogleLang(http.Controller):
#     @http.route('/google_lang/google_lang/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/google_lang/google_lang/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('google_lang.listing', {
#             'root': '/google_lang/google_lang',
#             'objects': http.request.env['google_lang.google_lang'].search([]),
#         })

#     @http.route('/google_lang/google_lang/objects/<model("google_lang.google_lang"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('google_lang.object', {
#             'object': obj
#         })
