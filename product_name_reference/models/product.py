# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.multi
    def name_get(self):
        return [(record.id, record.default_code or record.name) for record in self]


class Product(models.Model):
    _inherit = 'product.product'

    @api.multi
    def name_get(self):
        return [(record.id, record.default_code or record.name) for record in self]
