# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

{
    'name': 'Margins by Product Template',
    'summary': 'Add to the product template a button to access to Product Margins wizard provide by product_margin module.',
    'author': 'Critech Limited',
    'website': 'http://www.critech-services.com',
    'category': 'Product',
    'version': '9.0.1.0.0',
    'license': 'Other OSI approved licence',
    'depends': [
        'base',
        'product',
        'product_margin',
    ],
    'data': [
        'wizard/product_template_margin_view.xml'
    ],
    'installable': True,
    'application': False,
    'sequence':	100,
    'auto_install': False
}