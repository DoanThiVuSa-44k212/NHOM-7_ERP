from odoo import api, fields, models


class temporarywarehouse(models.Model):
    _name = "temporary.warehouse"

    name = fields.Char(string="Tên Kho", required=True)
    diachi = fields.Text(string="Địa chỉ")
    dientich = fields.Integer(string="Diện Tích Bãi")
    dientich1 = fields.Integer(string="Diện Tích Kho")
    succhua = fields.Integer(string="Sức Chứa (Tấn)")
    tongdt = fields.Integer(string="Tổng Diện Tích", compute="_compute_sum_price")
    tinhtrang = fields.Boolean(string='Có Thể Sử Dụng', default=True)

    def action_inactive(self):
        self.write({'tinhtrang': False})

    def action_active(self):
        self.write({'tinhtrang': True})

    def _compute_sum_price(self):
        for temporarywarehouse in self:
            tongdt = 0
        if temporarywarehouse.dientich and temporarywarehouse.dientich1:
            tongdt += (temporarywarehouse.dientich+ temporarywarehouse.dientich1)
        temporarywarehouse.tongdt = tongdt
