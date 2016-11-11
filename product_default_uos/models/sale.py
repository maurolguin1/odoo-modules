# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):
        result = super(SaleOrderLine, self).product_id_change()

        if self.product_id and self.product_id.uom_so_id and self.product_id != self.product_id.uom_so_id:
            self.update({
                'product_uom': self.product_id.uom_so_id,
                'price_unit': self.env['product.uom']._compute_price(
                    self.product_id.uom_po_id.id,
                    self.price_unit,
                    self.product_id.uom_so_id.id
                )
            })

        return result

