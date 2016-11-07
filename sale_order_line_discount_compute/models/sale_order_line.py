# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    x_price_unit = fields.Float(string='Unit Price', required=True, digits=dp.get_precision('Product Price'), default=0.0)

    @api.onchange('price_unit', 'product_id')
    def _onchange_copy_price(self):
        self.x_price_unit = self.price_unit

    @api.onchange('x_price_unit')
    def _onchange_compute_discount(self):
        if self.env.user.has_group('sale.group_discount_per_so_line'):
            try:
                self.discount = (self.price_unit - self.x_price_unit) / self.price_unit * 100
            except ZeroDivisionError:
                pass
        else:
            self.price_unit = self.x_price_unit
