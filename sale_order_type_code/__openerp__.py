# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

{
    'name': 'Sale Order Type Code',
    'summary': 'Add a unique code field for sale order type',
    'author': 'Critech Limited',
    'website': 'http://www.critech-services.com',
    'category': 'Sales Management',
    'version': '9.0.1.0.0',
    'license': 'Other OSI approved licence',
    'depends': [
        'base',
        'sale_order_type',
    ],
    'data': [
        'views/inherit_sale_order_type.sot_sale_order_type_form.xml',
    ],
    'post_init_hook': 'setup_default_code',
    'installable': True,
    'application': False,
    'sequence':	100,
    'auto_install': False
}
