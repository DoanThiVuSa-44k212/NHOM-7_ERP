from odoo import api, fields, models


class temporarywarehouse(models.Model):
    _name = "temporary.warehouse"

    name = fields.Char(string="Tên Kho", required=True)
    diachi = fields.Text (string="Địa chỉ")
    dientich = fields.Char(string="Diện Tích (Ha)")
