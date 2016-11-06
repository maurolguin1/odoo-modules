# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_uom_qty')
    def _onchange_compute_qty(self):
        product_uom = self.product_id.uom_id
        line_uom = self.product_uom
        line_uom_qty = self.product_uom_qty

        if product_uom.id != line_uom.id and product_uom.rounding == 1:
            product_uom_qty = self.env['product.uom']._compute_qty_obj(line_uom, line_uom_qty, product_uom)
            line_uom_qty = self.env['product.uom']._compute_qty_obj(product_uom, product_uom_qty, line_uom)

        self.product_uom_qty = line_uom_qty
