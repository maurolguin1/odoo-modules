# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    density = fields.Float(string='Density', digits=dp.get_precision('Density'))

    @api.onchange('density', 'volume')
    def _compute_weight(self):
        if not self.volume or not self.density:
            return False

        self.weight = self.volume * self.density


class Product(models.Model):
    _inherit = 'product.product'

    density = fields.Float(string='Density', digits=dp.get_precision('Density'))

    @api.onchange('density', 'volume')
    def _compute_weight(self):
        if not self.volume or not self.density:
            return False

        self.weight = self.volume * self.density
