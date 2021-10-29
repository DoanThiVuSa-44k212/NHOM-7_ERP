from odoo import api, fields, models

class Inventory(models.Model):
    _name = "stock.inventory"
    _inherit = "stock.inventory"
    _description = "RMA Product Preserve"

    # datebq=fields.Date(string='Ngày nhập kho bảo quản')
    Kho = fields.Selection([
        ('1', 'Kho 1'),
        ('2', 'Kho 2'),
        ('3', 'Kho 3'),
    ], required=True, default='1')

