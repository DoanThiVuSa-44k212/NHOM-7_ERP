from odoo import api, fields, models

class rmaproductpreserve(models.Model):
    _name = "rma.productpreserve"
    _description = "RMA Product Preserve"

    pname= fields.Many2many('product.template', string="Tên SP")
    Ma_Hang = fields.Integer(string='Mã hàng')
    datebq=fields.Date(string='Ngày nhập kho bảo quản')
    datehh = fields.Date(string='Ngày nhập kho hàng hóa')
    So_luong = fields.Integer(string='Số lượng')
    Kho = fields.Selection([
        ('1', 'Kho 1'),
        ('2', 'Kho 2'),
        ('3', 'Kho 3'),
    ], required=True, default='1')

