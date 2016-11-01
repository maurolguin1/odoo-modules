# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api


class SettingsSerial(models.TransientModel):
    _inherit = 'stock.config.settings'

    serial_prefix = fields.Char(string='Prefix')
    serial_suffix_sequence_code = fields.Char(string='Sequence code to use')

    @api.multi
    def set_serial_prefix(self):
        self._set_ir_config_parameter(key='serial.prefix', value=self.serial_prefix)

    @api.multi
    def get_default_serial_prefix(self):
        return {'serial_prefix': self._get_ir_config_parameter(key='serial.prefix', default='%(vendor)s-%(product)s-%(sequence)s')}

    @api.multi
    def set_serial_suffix_sequence_code(self):
        self._set_ir_config_parameter(key='serial.suffix.sequence_code', value=self.serial_suffix_sequence_code)

    @api.multi
    def get_default_serial_suffix_sequence_code(self):
        return {'serial_suffix_sequence_code': self._get_ir_config_parameter(key='serial.suffix.sequence_code', default='stock.lot.serial')}

    @api.model
    def _set_ir_config_parameter(self, key, value):
        self.env['ir.config_parameter'].set_param('stock_picking_nomenclature.' + key, value)

    @api.model
    def _get_ir_config_parameter(self, key, default):
        value = self.env['ir.config_parameter'].get_param('stock_picking_nomenclature.' + key, None)

        if value is None:
            value = default

        return value
