from odoo import api, fields, models

class rmamerchandiseinventory(models.Model):
    _name = "rma.merchandiseinventory"
    _description = "RMA Merchandise Inventory"

    name = fields.Char(string='Tên Sản Phẩm')
    type = fields.Text('Mã Sản Phẩm')
    quantity1 = fields.Integer('Số Lượng Hàng Tồn')
    quantity2 = fields.Integer('Số Lượng Xuất Hàng')
    quantity3 = fields.Integer('Số Lượng Nhập Hàng')
    quantity4 = fields.Integer('Số Lượng Hàng Hỏng')
    Fact = fields.Char('Kiểm thực tế')
    difference = fields.Char('Chênh Lệch')
    date = fields.Date('Ngày Kiểm')
    description = fields.Text("Mô Tả Tình Trạng")
