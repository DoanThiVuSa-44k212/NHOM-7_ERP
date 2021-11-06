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
    Kho = fields.Many2one('temporary.warehouse', String="Nơi Bảo Quản")
    diachi = fields.Text(related="Kho.diachi", string="Địa chỉ")
    dientich = fields.Char(related="Kho.dientich", string="Diện Tích (Ha)")


class productpreverselines(models.Model):

    _name = "product.preserve.lines"
    # nhanbiet = fields.Char(string="nhanbiet")
    product_id = fields.Many2one('product.template', string="Tên Sản Phẩm")
    product_qty = fields.Integer(string="Số Lượng")
    list_price = fields.Float(string='Giá Bán', related="product_id.list_price")
    sum_price = fields.Integer(string="Tổng Tiền", compute="_compute_sum_price")
    preserve_id = fields.Many2one('product.preserve', string="Product Preserve")
    # test = fields.Integer(string="Số Lượng Hiện tại", compute="_compute_test")


    def _compute_sum_price(self):
        for productpreverselines in self:
          sum_price = 0
          if productpreverselines.product_id and productpreverselines.product_id.list_price:
             sum_price += (productpreverselines.product_id.list_price
                           * productpreverselines.product_qty)
          productpreverselines.sum_price = sum_price

    # @api.onchange("test")
    # def _compute_test(self):
    #     chang_qty = self.env['stock.picking']
    #     for productpreverselines in self:
    #         tested = chang_qty.product_qtyy
    #         if productpreverselines.product_qty and chang_qty.product_qtyy:
    #             tested += (productpreverselines.product_qty - chang_qty.product_qtyy)
    #         productpreverselines.test = tested
