{
    'name': 'RMA BIBICA',
    'version': '1.0',
    'summary': 'Return Merchandise Authorization',
    'sequence': -10,
    'description': """RMA BIBICA""",
    'category': 'Productivity',
    'license': 'LGPL-3',
    'depends': [
        'product',
        'stock',
        'uom'
    ],
    'data': [
        'Views/Products.xml',
        'Views/product_type.xml',
        'Views/scrap_goods.xml',
        'Views/productpreserve.xml',
        'Views/receive_returned_goods.xml',
        'Menu/Menu.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
