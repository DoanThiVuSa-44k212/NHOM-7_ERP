from odoo import api, fields, models


class productpreverse(models.Model):
    _name = "product.preserve"

    _description = "RMA Product Preserve"

    name = fields.Char(String="Tên Nghiệp Vụ")
    preserve_lines = fields.One2many('product.preserve.lines', 'preserve_id', string="Product Preserve")
    company_id = fields.Many2one('res.company',string="Công Ty")

    Nhietdo = fields.Selection([
        ('1', '10c->20c'),
        ('2', '20c->30c'),
    ], string="Nhiệt độ bảo quản", required=True, default='1')
    datebq = fields.Date(string='Ngày nhập kho bảo quản')
    datehh = fields.Date(string='Ngày nhập kho hàng hóa')
    thoigianbaoquan = fields.Date(string='Thời gian bảo quản')
    Kho = fields.Selection([
        ('1', 'Kho 1'),
        ('2', 'Kho 2'),
        ('3', 'Kho 3'),
    ], string="Nơi bảo quản", required=True, default='1')


class productpreverselines(models.Model):
    _name = "product.preserve.lines"
    product_id = fields.Many2one('product.template', string="Tên Sản Phẩm")
    product_qty = fields.Integer(string="Số Lượng")
    preserve_id = fields.Many2one('product.preserve', string ="Product Preserve")