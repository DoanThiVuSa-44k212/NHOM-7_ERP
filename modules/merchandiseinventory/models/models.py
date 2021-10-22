from odoo import api, fields, models, _, tools


class merchandise_inventory(models.Model):
    _name = "merchandise_inventory.merchandise_inventory"
    _description = "Merchandise Inventory"

    name = fields.Char(string='Tên Sản Phẩm')
    type = fields.Text('Mã Sản Phẩm')
    quantity1 = fields.Interger('Số Lượng Hàng Tồn')
    quantity2 = fields.Interger('Số Lượng Xuất Hàng')
    quantity3 = fields.Interger('Số Lượng Nhập Hàng')
    quantity4 = fields.Interger('Số Lượng Hàng Hỏng')
    Fact = fields.Char('Kiểm thực tế')
    difference = fields.Char('Chênh Lệch')
    date = fields.Date('Ngày Kiểm')
    description = fields.Text("Mô Tả Tình Trạng")

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100