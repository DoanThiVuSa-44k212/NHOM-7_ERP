# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    wage = fields.Integer(string='Wage')