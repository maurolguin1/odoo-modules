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

        if self.product_id:
            if self.product_id.description_sale:
                self.update({'name': self.product_id.description_sale})

        return result
