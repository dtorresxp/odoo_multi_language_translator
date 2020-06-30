# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class google_lang(models.Model):
#     _name = 'google_lang.google_lang'
#     _description = 'google_lang.google_lang'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
