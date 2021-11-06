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
    pr_type = fields.Many2one(comodel_name='product.type', related="product_id.pr_type", string="Loại Sản Phẩm", delegate=True)
    list_price = fields.Float(string='Giá Bán', related ="product_id.list_price")
    weight = fields.Float(related ="product_id.weight", string='Cân Nặng')