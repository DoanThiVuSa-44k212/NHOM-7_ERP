# -*- coding: utf-8 -*-
# from odoo import http


# class MerchandiseInventory(http.Controller):
#     @http.route('/merchandise_inventory/merchandise_inventory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/merchandise_inventory/merchandise_inventory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('merchandise_inventory.listing', {
#             'root': '/merchandise_inventory/merchandise_inventory',
#             'objects': http.request.env['merchandise_inventory.merchandise_inventory'].search([]),
#         })

#     @http.route('/merchandise_inventory/merchandise_inventory/objects/<model("merchandise_inventory.merchandise_inventory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('merchandise_inventory.object', {
#             'object': obj
#         })
