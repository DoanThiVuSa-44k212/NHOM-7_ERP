from odoo import api, fields, models, tools, _


class stockPicking  (models.Model):
    _name = 'stock.picking'
    _inherit = 'stock.picking'

    image = fields.Binary(string="Hình Ảnh")
    quantity = fields.Integer(string="Số Lượng")
    reason = fields.Char(string="Lí Do Trả Hàng")
    description = fields.Text(string="Mô Tả Tình Trạng Hàng Hóa ")
    address_name = fields.Text(string="Địa Chỉ Công Ty")
    delegate_name = fields.Char(string="Tên Đại Diện Công Ty Trả Hàng")
    phone = fields.Integer(string="Số Điện Thoại")
    emai = fields.Text(string="Email")
    status = fields.Selection([
        ("chapnhan", "Chấp Nhận"),
        ("khongchapnhan", "Không Chấp Nhận"),
    ], string="Trạng Thái", default=False)

    # product_idd = fields.Many2one('product.template', string="Tên Sản Phẩm")
    # product_qtyy = fields.Integer(string="Số Lượng")
    # nhanbiet = fields.Char(string="nhanbiet")


