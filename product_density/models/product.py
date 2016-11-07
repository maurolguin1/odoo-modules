# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    density = fields.Float(string='Density', digits=dp.get_precision('Density'))

    @api.onchange('surface', 'density')
    def _compute_weight(self):
        if not self.surface or not self.density:
            return False

        self.weight = self.surface * self.density


class Product(models.Model):
    _inherit = 'product.product'

    density = fields.Float(string='Density', digits=dp.get_precision('Density'))

    @api.onchange('surface', 'density')
    def _compute_weight(self):
        if not self.surface or not self.density:
            return False

        self.weight = self.surface * self.density
