# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, _


class SaleOrderType(models.Model):
    _inherit = 'sale.order.type'

    code = fields.Char(string='Code', required=True)

    _sql_constraints = [
        ('code_uniq', 'unique (code)', _('The Sale Order Type "code" must be unique')),
    ]

