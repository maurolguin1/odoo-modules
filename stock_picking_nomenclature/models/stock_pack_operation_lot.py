# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api
from slugify import slugify


class StockPackOperationLot(models.Model):
    _inherit = 'stock.pack.operation.lot'

    lot_name = fields.Char(default=lambda self: self.get_default_name())

    @api.model
    def get_default_name(self):
        operation_id = self.env.context.get('operation_id')

        if not operation_id:
            return ''

        operation = self.env['stock.pack.operation'].browse(operation_id)

        if operation.product_id.tracking == 'lot':
            return self._get_default_lot_name(operation=operation)

        if operation.product_id.tracking == 'serial':
            return self._get_default_serial_name(operation=operation)

        return ''

    @api.multi
    def write(self, vals):
        # Synchronize stock.pack.operation.lot.lot_name with the real serial number ;
        # ie the one we create with a sequence number suffix

        for record in self:
            if not record.lot_id and vals.get('lot_id', False):
                lot = self.env['stock.production.lot'].browse(vals.get('lot_id'))
                vals.update({'lot_name': lot.name})

            super(StockPackOperationLot, record).write(vals)

        return True

    @api.model
    def _get_default_lot_name(self, operation):
        if operation.picking_id.partner_id and operation.picking_id.partner_id.ref:
            partner_ref = operation.picking_id.partner_id.ref
        else:
            partner_ref = slugify(operation.picking_id.partner_id.name)

        if operation.product_id and operation.product_id.default_code:
            product_code = operation.product_id.default_code
        else:
            product_code = slugify(operation.product_id.name)

        return self.env['ir.config_parameter'].get_param('stock_picking_nomenclature.lot.prefix') % {
            'vendor': partner_ref,
            'product': product_code
        }

    @api.model
    def _get_default_serial_name(self, operation):
        if operation.picking_id.partner_id and operation.picking_id.partner_id.ref:
            partner_ref = operation.picking_id.partner_id.ref
        else:
            partner_ref = slugify(operation.picking_id.partner_id.name)

        if operation.product_id and operation.product_id.default_code:
            product_code = operation.product_id.default_code
        else:
            product_code = slugify(operation.product_id.name)

        prefix_pattern = self.env['ir.config_parameter'].get_param('stock_picking_nomenclature.serial.prefix')
        seq_number = ''

        if prefix_pattern.find('%(sequence)s') >= 0:
            seq_code = self.env['ir.config_parameter'].get_param('stock_picking_nomenclature.serial.suffix.sequence_code')
            seq_number = self.env['ir.sequence'].next_by_code(seq_code)

        return prefix_pattern % {
            'vendor': partner_ref,
            'product': product_code,
            'sequence': seq_number,
        }
