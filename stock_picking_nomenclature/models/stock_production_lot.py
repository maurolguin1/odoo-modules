# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    @api.model
    def create(self, vals):
        # If we create a serial from picking operation
        if self.env.context.get('default_picking_type_id', False):
            product_id = vals.get('product_id', False)
            product = self.env['product.product'].browse(product_id)

            # Append sequence only for lot, not for serial
            if product.tracking == 'lot' and self.env['ir.config_parameter'].get_param('stock_picking_nomenclature.lot.suffix.active'):
                seq_code = self.env['ir.config_parameter'].get_param('stock_picking_nomenclature.lot.suffix.sequence_code')
                seq_number = self.env['ir.sequence'].next_by_code(seq_code)

                vals.update({'name': vals.get('name') + seq_number})

        return super(StockProductionLot, self).create(vals)
