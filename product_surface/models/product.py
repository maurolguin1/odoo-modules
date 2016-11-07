# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp


class Product(models.Model):
    _inherit = 'product.product'

    surface = fields.Float(string='Surface', compute='_compute_surface', store=True, digits=dp.get_precision('Surface'))

    @api.multi
    @api.depends('order_line.x_cost_subtotal')
    def _compute_cost_subtotal(self):
        for record in self:
            record.x_cost_subtotal = sum(line.x_cost_subtotal for line in record.order_line)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    surface = fields.Float(string='Surface', compute='_compute_surface', store=True, digits=dp.get_precision('Surface'))

    @api.multi
    @api.depends('length', 'width', 'dimensional_uom_id')
    def _compute_surface(self):
        for record in self:
            if not record.length or not record.width or not record.dimensional_uom_id:
                return False

            length_m = self.convert_to_meters(record.length, record.dimensional_uom_id)
            width_m = self.convert_to_meters(record.width, record.dimensional_uom_id)

            record.surface = length_m * width_m
