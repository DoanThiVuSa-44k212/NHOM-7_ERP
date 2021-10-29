from odoo import api, fields, models

class producttype(models.Model):
    _name = "product.type"
    _description = "Product Type"

    name = fields.Char(string="Loại sản phẩm", tracking=True, delegate=True)
    unit_of_measure = fields.Many2one('uom.uom', string='Đơn Vị Tính')
    description = fields.Text(string="Mô Tả")