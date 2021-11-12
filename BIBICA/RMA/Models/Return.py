from odoo import api, fields, models, tools, _


class stockPicking(models.Model):
    _name = 'stock.picking'
    _inherit = 'stock.picking'

    image = fields.Binary(string="Hình Ảnh")
    malohang = fields.Char(string="Mã Lô Hàng")
    create_date = fields.Date(string="Ngày Tạo Phiếu", default=lambda self: fields.Date.today())
    quantity = fields.Integer(string="Số Lượng")
    reason = fields.Selection([
        ('1', 'Chỉ Số Thành Phần Không Giống Mô Tả'),
        ('2', 'Sai Sản Phẩm'),
        ('3', 'Hàng Hư Hỏng Trong Quá Trình Vận Chuyển'),
        ('4', 'Hàng Bị Hết Hạn Sử Dụng'),
        ('5', 'Khác')
    ], string="Lí Do Trả Hàng", required=True)
    khac = fields.Char(string="Khác")
    tp_line = fields.One2many('product.tp.lines', 'thanhphan_id')
    description = fields.Text(string="Mô Tả Tình Trạng Thực Tế ")
    address_name = fields.Text(string="Địa Chỉ Công Ty")
    phone = fields.Integer(string="Số Điện Thoại")
    email = fields.Text(string="Email")
    make_vote = fields.Many2one('hr.employee', string='Người Tạo Phiếu', required=True)
    ship = fields.Selection([
        ("thuenguoichuyen", "Thuê Đơn Vị Vận Chuyển "),
        ("denkhonhantructiep", " Đến Kho Nhận Trực Tiếp"), ],
        string="Phương Thức Vận Chuyển", default=False)

    status = fields.Selection([
        ("chapnhan", "Chấp Nhận"),
        ("khongchapnhan", "Không Chấp Nhận"),
    ], string="Trạng Thái", default=False)
    httt = fields.Selection([
        ("chuyenkhoan", "Chuyển khoản"),
        ("tienmat", "Tiền mặt"),
    ], string="Phương Thức Thanh Toán", default=False)


class ProductTPLines(models.Model):
    _name = 'product.tp.lines'

    product = fields.Many2one('product.template', string='Tên Sản Phẩm')
    tentp = fields.Many2one('product.ingredients', string="Tên Thành Phần")
    soluongtt = fields.Integer(string="Tỷ Lệ % Thực Tế")
    ghichu = fields.Text(string="Ghi Chú")
    thanhphan_id = fields.Many2one('stock.picking')
