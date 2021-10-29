# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    weight = fields.Integer(string='Cân Nặng')
    pr_type = fields.Many2one(comodel_name='product.type', string="Loại Sản Phẩm", delegate=True)
    unit_of_measure = fields.Many2one('uom.uom', related="pr_type.unit_of_measure", string='Đơn Vị Tính')
