# -*- coding: utf-8 -*-
{
    'name': 'MERCHANDISE INVENTORY',
    'version': '1.0',
    'summary': 'Inventory',
    'sequence': 16,
    'description': """App Kiểm Kê Hàng Hóa""",
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/models.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
