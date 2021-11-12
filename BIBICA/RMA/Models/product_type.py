from odoo import api, fields, models

class productcategory(models.Model):
    _name = "product.category"
    _inherit = "product.category"

    unit_of_measure = fields.Many2one('uom.uom', string='Đơn Vị Tính')
    description = fields.Text(string="Mô Tả")
