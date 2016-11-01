# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

{
    'name': 'Stock picking nomenclature',
    'summary': 'During picking operation, generate name of lot or serial number for purchased product',
    'author': 'Critech Limited',
    'website': 'http://www.critech-services.com',
    'category': 'Stock',
    'version': '9.0.1.0.0',
    'license': 'Other OSI approved licence',
    'depends': [
        'base',
        'stock',
    ],
    'external_dependencies': {
        'python': [
            'slugify'
        ]
    },
    'data': [
        'data/ir_sequence.xml',
        'data/config_parameter.xml',
        'views/inherit_stock.pack_operation_lot_form_view.xml',
        'views/inherit_stock.res_config_lot_view.xml',
        'views/inherit_stock.res_config_serial_view.xml',
    ],
    'installable': True,
    'application': False,
    'sequence':	100,
    'auto_install': False,
}

