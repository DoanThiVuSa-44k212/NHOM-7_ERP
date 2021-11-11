from odoo import api, fields, models


class productpreverse(models.Model):
    _name = "product.preserve"
    _description = "RMA Product Preserve"

    name = fields.Char(String="Tên Nghiệp Vụ")
    preserve_lines = fields.One2many('product.preserve.lines', 'preserve_id', string="Product Preserve")
    company_id = fields.Many2one('res.company', string="Công Ty")

    Nhietdo = fields.Selection([
        ('1', '10c->20c'),
        ('2', '20c->30c'),
    ], string="Nhiệt độ bảo quản", required=True, default='1')
    datebq = fields.Date(string='Ngày nhập kho bảo quản')
    datehh = fields.Date(string='Ngày nhập kho hàng hóa')
    thoigianbaoquan = fields.Date(string='Thời gian bảo quản')
    datechamsocdinhki = fields.Date(string='Ngày theo dõi hàng hóa định kì')
    Kho = fields.Many2one('temporary.warehouse', String="Nơi Bảo Quản")
    diachi = fields.Text(related="Kho.diachi", string="Địa chỉ")
    dientich = fields.Integer(related="Kho.dientich", string="Diện Tích")
    dientich1 = fields.Integer(related="Kho.dientich1", string="Diện Tích")
    tinhtranghang = fields.Selection([
        ('1', 'Dưới 40%'),
        ('2', 'Trên 40%'),
    ], string="Tình trạng hàng", required=True, default='1')


class productpreverselines(models.Model):

    _name = "product.preserve.lines"
    product_id = fields.Many2one('product.template', string="Tên Sản Phẩm")
    product_qty = fields.Integer(string="Số Lượng")
    list_price = fields.Float(string='Giá Bán', related="product_id.list_price")
    sum_price = fields.Integer(string="Tổng Tiền", compute="_compute_sum_price")
    preserve_id = fields.Many2one('product.preserve', string="Product Preserve")


    def _compute_sum_price(self):
        for productpreverselines in self:
          sum_price = 0
          if productpreverselines.product_id and productpreverselines.product_id.list_price:
             sum_price += (productpreverselines.product_id.list_price
                           * productpreverselines.product_qty)
          productpreverselines.sum_price = sum_price
