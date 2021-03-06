# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

{
    'name': 'Sale Order Stats',
    'summary': 'Display stats relative to the sale order',
    'author': 'Critech Limited',
    'website': 'http://www.critech-services.com',
    'category': 'Sales Management',
    'version': '9.0.1.0.0',
    'license': 'Other OSI approved licence',
    'depends': [
        'base',
        'sale',
        'decimal_precision',
    ],
    'data': [
        'views/inherit_sale.view_order_form.xml',
        'views/inherit_sale.view_res_config.xml',
        'views/static.xml',
    ],
    'installable': True,
    'application': False,
    'sequence':	100,
    'auto_install': False
}
