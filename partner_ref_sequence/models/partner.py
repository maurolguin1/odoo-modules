# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    ref = fields.Char(copy=False)

    @api.model
    def create(self, vals):
        if vals.get('is_company', False):
            return super(Partner, self).create(vals)

        if not vals.get('ref') and vals.get('supplier', False):
            vals.update({'ref': self._get_vendor_ref()})

        if not vals.get('ref') and vals.get('customer', False):
            vals.update({'ref': self._get_client_ref()})

        return super(Partner, self).create(vals)

    @api.model
    def _get_vendor_ref(self):
        return self.env['ir.sequence'].next_by_code('partner.vendor_ref')

    @api.model
    def _get_client_ref(self):
        return self.env['ir.sequence'].next_by_code('partner.client_ref')

