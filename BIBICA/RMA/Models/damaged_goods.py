from odoo import api, fields, models, tools


class Damaged_goods(models.Model):
    _name = "damaged.goods"

    name = fields.Many2many('product.template', 'name', String="Tên Sản Phẩm")
    processing_date = fields.Date(string="Ngày Xử Lý Hàng Hóa")
    quantity = fields.Integer(string="Số Lượng")
    input_date = fields.Date(string="Ngày Nhập Kho Sản Phẩm")
    description = fields.Text(string="Mô Tả")
    status = fields.Selection([
        ("tieuhuy", "Tiêu Hủy"),
        ("xahang", "Xả Hàng"),
    ], string="Trạng Thái", default=False)
