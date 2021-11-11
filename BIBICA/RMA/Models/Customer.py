
from odoo import api, fields, models, tools, _


class respartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    cmnd = fields.Char(string="CMND")
    ngayhoptac = fields.Date(string="Ngày Hợp Tác", default = lambda self: fields.Date.today ())
    fax = fields.Char(string="Fax")
    linhvuc = fields.Char(string="Lĩnh Vực")
    lhpl = fields.Selection([
        ('1', 'Công Ty TNHH Một Thành Viên'),
        ('2', 'Công Ty TNHH Hai Thành Viên'),
        ('3', 'Công Ty Cổ Phần'),
        ('4', 'Công Ty Hợp Danh'),
        ('5', 'Doanh Nghiệp Tư Nhân'),
    ], string="Loại Hình Pháp Lý")
    donhang_count = fields.Integer(string='Số Đơn Hàng Trả Lại', compute='compute_count_cus')
    active = fields.Boolean(string='Còn Liên Lạc', default=True)

    def compute_count_cus(self):
        donhang_count= self.env['stock.picking'].search_count([('partner_id', '=', self.id)])
        self.donhang_count = donhang_count

    def action_inactive(self):
        self.write({'active': False})

    def action_active(self):
        self.write({'active': True})


