from odoo import api, fields, models


class productingredients(models.Model):
    _name = "product.ingredients"

    name = fields.Char(string="Tên Thành Phần", required=True)
    dang = fields.Selection([
        ('Bot', 'Bột'),
        ('nuoc', 'Nước'),
        ('vien', 'Viên'),
        ('hat', 'Hạt'),
    ], string="Dạng Thành Phần", required=True, Default='Bot')
    tusx = fields.Boolean(string="Có Thể Sản Xuất")
    congdung = fields.Text(string="Công Dụng")
    ghichu = fields.Text(string="Ghi Chú")
