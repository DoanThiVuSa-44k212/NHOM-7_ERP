# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    wage = fields.Integer(string='Wage')