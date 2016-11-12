# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_comment = fields.Text(string='Customer Comment')

