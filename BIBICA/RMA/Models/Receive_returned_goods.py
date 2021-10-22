from odoo import api, fields, models, tools


class Returned_goods(models.Model):
    _name = "Returned.goods"

    name = fields.Many2many('product.template', 'name', String="Tên Sản Phẩm")
    input_date = fields.Date(string="Ngày Nhận Hàng Hóa")
    quantity = fields.Integer(string="Số Lượng")
    import_date= fields.Date(string="Ngày Nhập Hàng Hóa")
    export_date = fields.Date(string="Ngày Xuất Hàng Hóa")
    expiry_date = fields.Date(string="Hạn Sử Dụng Hàng Hóa")
    company_name = fields.Text(string="Tên Công Ty Trả Hàng")
    address_name=fields.Text(string="Địa Chỉ Công Ty")
    delegate_name=fields.Char(string="Tên Đại Diện Công Ty Trả Hàng")
    phone=fields.Integer(string="Số Điện Thoại")
    emai= fields.Text(string="Email")
    description= fields.Text(string="Mô Tả Tình Trạng Hàng Hóa ")
    status = fields.Selection([
        ("chapnhan", "Chấp Nhận"),
        ("khongchapnhan", "Không Chấp Nhận"),
    ], string="Trạng Thái", default=False)

