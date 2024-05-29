# -*- coding: utf-8 -*-
{
    'name': 'Disable Sale Picking',
    'version': '17.0.1.0.0',
    'summary': 'Disable Sale Picking',
    'description': """Disable Sale Picking
        """,
    'category': 'Inventory/Inventory',
    'depends': ['sale_management', 'stock'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
