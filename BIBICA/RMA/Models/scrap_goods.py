from odoo import api, fields, models, tools, _

class StockScrap(models.Model):
    _name = 'stock.scrap'
    _inherit = ['stock.scrap']

    product_status = fields.Selection([
        ('tieuhuy', 'Tiêu Hủy'),
        ('xahang', 'Xả Hàng'),
    ], string="Trạng Thái", required=True, default='tieuhuy')

    description = fields.Text ()
    input_date = fields.Date(string="Ngày Nhập Kho Sản Phẩm")
    processing_date = fields.Date(string="Ngày Xử Lý Hàng Hóa")
    employee = fields.Many2many('hr.employee', string='Tên Nhân Viên', required=True)
    image = fields.Binary(string="Hình Ảnh")
    note = fields.Text(string="Ghi Chú")
    categ_id = fields.Many2one('product.category',related="product_id.categ_id", string='Danh Mục Sản Phẩm',)
    list_price = fields.Float(string='Giá Bán', related ="product_id.list_price")