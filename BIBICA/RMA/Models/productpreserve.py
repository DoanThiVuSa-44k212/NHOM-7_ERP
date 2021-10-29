from odoo import api, fields, models

class Inventory(models.Model):
    _name = "stock.inventory"
    _inherit = "stock.inventory"
    _description = "RMA Product Preserve"

    # datebq=fields.Date(string='Ngày nhập kho bảo quản')
    Nhietdo=fields.Selection([
        ('1', '10c->20c'),
        ('2', '20c->30c'),
    ],string="Nhiệt độ bảo quản", required=True, default='1')
    datebq=fields.Date(string='Ngày nhập kho bảo quản')
    datehh=fields.Date(string='Ngày nhập kho hàng hóa')
    thoigianbaoquan = fields.Date(string='Thời gian bảo quản')
    Kho = fields.Selection([
        ('1', 'Kho 1'),
        ('2', 'Kho 2'),
        ('3', 'Kho 3'),
    ],string="Nơi bảo quản", required=True, default='1')


