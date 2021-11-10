from odoo import api, fields, models, tools, _


class stockPicking  (models.Model):
    _name = 'stock.picking'
    _inherit = 'stock.picking'

    image = fields.Binary(string="Hình Ảnh")
    malohang = fields.Char(string="Mã Lô Hàng")
    create_date=fields.Datetime(string="Ngày Tạo Phiếu")
    quantity = fields.Integer(string="Số Lượng")
    reason = fields.Char(string="Lí Do Trả Hàng")
    description = fields.Text(string="Mô Tả Tình Trạng Thực Tế ")
    address_name = fields.Text(string="Địa Chỉ Công Ty")
    delegate_name = fields.Char(string="Tên Công Ty Trả Hàng")
    phone = fields.Integer(string="Số Điện Thoại")
    email = fields.Text(string="Email")
    make_vote = fields.Many2one('hr.employee', string='Người Tạo Phiếu', required=True)
    ship=fields.Selection([
        ("thuenguoichuyen", "Thuê Đơn Vị Vận Chuyển "),
        ("denkhonhantructiep"," Đến Kho Nhận Trực Tiếp"),],
        string="Phương Thức Vận Chuyển",default=False)

    status = fields.Selection([
        ("chapnhan", "Chấp Nhận"),
        ("khongchapnhan", "Không Chấp Nhận"),
    ], string="Trạng Thái", default=False)
    httt = fields.Selection([
        ("chuyenkhoan", "Chuyển khoản"),
        ("tienmat", "Tiền mặt"),
    ], string="Phương Thức Thanh Toán", default=False)





