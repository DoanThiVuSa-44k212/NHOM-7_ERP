# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    weight = fields.Integer(string='Cân Nặng')
    pr_type = fields.Many2one(comodel_name='product.category', string="Loại Sản Phẩm", delegate=True)
    unit_of_measure = fields.Many2one('uom.uom', related="pr_type.unit_of_measure", string='Đơn Vị Tính')
    hansudung = fields.Char(string="Hạn Sử Dụng")
    baohanh = fields.Char(string="Bảo Hành")
    thanhphan_lines = fields.One2many('product.template.lines', 'thanhphan_id')
    trahang_count = fields.Integer(string='Số Đơn Hàng Trả Lại', compute='compute_count_cus')

    def compute_count_cus(self):
        trahang_count= self.env['stock.picking'].search_count([('product_id', '=', self.name)])
        self.trahang_count = trahang_count

class ProductTemplateLines(models.Model):
    _name = 'product.template.lines'

    tentp = fields.Many2one('product.ingredients', string="Tên Thành Phần")
    soluong = fields.Integer(string="Tỷ Lệ %")
    congdung = fields.Text(related="tentp.congdung", string="Công Dụng")
    thanhphan_id = fields.Many2one('product.template')

