# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

{
    'name': 'Product Surface',
    'summary': 'Add surface to products ; based on width and length from product_dimension',
    'author': 'Critech Limited',
    'website': 'http://www.critech-services.com',
    'category': 'Sales Management',
    'version': '9.0.1.0.0',
    'license': 'Other OSI approved licence',
    'depends': [
        'base',
        'product',
        'product_dimension',
        'decimal_precision',
    ],
    'data': [
        'data/decimal_precision.xml',
        'views/inherit_product_dimension.product_normal_form_view.xml',
        'views/inherit_product_dimension.product_template_only_form_view.xml',
    ],
    'installable': True,
    'application': False,
    'sequence':	100,
    'auto_install': False
}
