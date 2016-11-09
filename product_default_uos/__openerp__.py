# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

{
    'name': 'Product Default Unit of Sale',
    'summary': 'Ability to set a default unit of measure used for sell product',
    'author': 'Critech Limited',
    'website': 'http://www.critech-services.com',
    'category': 'Sales Management',
    'version': '9.0.1.0.0',
    'license': 'Other OSI approved licence',
    'depends': [
        'base',
        'product',
        'sale',
    ],
    'data': [
        'views/inherit_product.product_template_only_form_view.xml',
    ],
    'post_init_hook': 'setup_default_uom_so',
    'installable': True,
    'application': False,
    'sequence':	100,
    'auto_install': False
}
