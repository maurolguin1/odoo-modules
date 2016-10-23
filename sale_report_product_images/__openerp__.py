# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

{
    'name': 'Sale Reports Product Images',
    'summary': 'Display the product image in sale reports',
    'author': 'Critech Limited',
    'website': 'http://www.critech-services.com',
    'category': 'Sales Management',
    'version': '9.0.1.0.0',
    'license': 'Other OSI approved licence',
    'depends': [
        'sale'
    ],
    'data': [
        'views/report.xml'
    ],
    'installable': True,
    'application': False,
    'sequence':	100,
    'auto_install': False
}
