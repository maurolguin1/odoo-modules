# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

{
    'name': 'Sale Order Customer Comment',
    'summary': 'Add a new field in Sale Order for the customer comment',
    'author': 'Critech Limited',
    'website': 'http://www.critech-services.com',
    'category': 'Sales Management',
    'version': '9.0.1.0.0',
    'license': 'Other OSI approved licence',
    'depends': [
        'base',
        'sale',
    ],
    'data': [
        'views/inherit_sale.view_order_form.xml',
    ],
    'installable': True,
    'application': False,
    'sequence':	100,
    'auto_install': False
}
