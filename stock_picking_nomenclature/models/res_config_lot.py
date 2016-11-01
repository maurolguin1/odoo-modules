# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api


class SettingsLot(models.TransientModel):
    _inherit = 'stock.config.settings'

    lot_prefix = fields.Char(string='Prefix')
    lot_suffix_active = fields.Boolean(string='Suffix sequence')
    lot_suffix_sequence_code = fields.Char(string='Sequence code to use')

    @api.multi
    def set_lot_prefix(self):
        self._set_ir_config_parameter(key='lot.prefix', value=self.lot_prefix)

    @api.multi
    def get_default_lot_prefix(self):
        return {'lot_prefix': self._get_ir_config_parameter(key='lot.prefix', default='%(vendor)s-')}

    @api.multi
    def set_lot_suffix_active(self):
        self._set_ir_config_parameter(key='lot.suffix.active', value=self.lot_suffix_active)

    @api.multi
    def get_default_lot_suffix_active(self):
        return {'lot_suffix_active': self._get_ir_config_parameter(key='lot.suffix.active', default=True)}

    @api.multi
    def set_lot_suffix_sequence_code(self):
        self._set_ir_config_parameter(key='lot.suffix.sequence_code', value=self.lot_suffix_sequence_code)

    @api.multi
    def get_default_lot_suffix_sequence_code(self):
        return {'lot_suffix_sequence_code': self._get_ir_config_parameter(key='lot.suffix.sequence_code', default='stock_picking_nomenclature.lot.suffix_sequence')}

    @api.model
    def _set_ir_config_parameter(self, key, value):
        self.env['ir.config_parameter'].set_param('stock_picking_nomenclature.' + key, value)

    @api.model
    def _get_ir_config_parameter(self, key, default):
        value = self.env['ir.config_parameter'].get_param('stock_picking_nomenclature.' + key, None)

        if value is None:
            value = default

        return value
