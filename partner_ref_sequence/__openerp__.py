# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

{
    'name': 'Partner Reference Sequence',
    'summary': 'Setup sequence for partner internal reference',
    'author': 'Critech Limited',
    'website': 'http://www.critech-services.com',
    'category': 'Others',
    'version': '9.0.1.0.0',
    'license': 'Other OSI approved licence',
    'depends': [
        'base',
    ],
    'data': [
        'data/partner_default_ref.xml',
    ],
    'installable': True,
    'application': False,
    'sequence':	100,
    'auto_install': False,
}
