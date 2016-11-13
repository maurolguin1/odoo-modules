# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields
from openerp.addons import decimal_precision as dp


class Product(models.Model):
    _inherit = 'product.product'

    volume = fields.Float(digits=dp.get_precision('Volume'))


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    volume = fields.Float(digits=dp.get_precision('Volume'))

