# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_amount_untaxed = fields.Monetary(string='Turnover', related='amount_untaxed')
    x_cost_subtotal = fields.Float(string='Cost subtotal', compute='_compute_cost_subtotal', store=True, digits_compute=dp.get_precision('Product Price'))
    x_margin_amount = fields.Float(string='Margin amount', compute='_compute_margin_amount', store=True, digits_compute=dp.get_precision('Product Price'))
    x_margin_rate = fields.Float(string='Margin rate', compute='_compute_margin_rate', store=True, digits_compute=dp.get_precision('Product Price'))
    x_markup_rate = fields.Float(string='Markup rate', compute='_compute_markup_rate', store=True, digits_compute=dp.get_precision('Product Price'))
    x_discount_amount = fields.Float(string='Discount amount', compute='_compute_discount_amount', store=True, digits_compute=dp.get_precision('Product Price'))
    x_discount_rate = fields.Float(string='Discount rate', compute='_compute_discount_rate', store=True, digits_compute=dp.get_precision('Product Price'))

    @api.multi
    @api.depends('order_line.x_cost_subtotal')
    def _compute_cost_subtotal(self):
        for record in self:
            record.x_cost_subtotal = sum(line.x_cost_subtotal for line in record.order_line)

    @api.multi
    @api.depends('order_line.x_margin_amount')
    def _compute_margin_amount(self):
        for record in self:
            record.x_margin_amount = sum(line.x_margin_amount for line in record.order_line)

    @api.multi
    @api.depends('order_line.x_margin_rate')
    def _compute_margin_rate(self):
        for record in self:
            try:
                record.x_margin_rate = sum(line.x_margin_rate for line in record.order_line) / self._order_line_with_qty_len(record=record)
            except ZeroDivisionError:
                record.x_margin_rate = 0

    @api.multi
    @api.depends('order_line.x_margin_rate')
    def _compute_markup_rate(self):
        for record in self:
            try:
                record.x_markup_rate = sum(line.x_markup_rate for line in record.order_line) / self._order_line_with_qty_len(record=record)
            except ZeroDivisionError:
                record.x_markup_rate = 0

    @api.multi
    @api.depends('order_line.price_unit', 'order_line.price_reduce', 'order_line.product_uom_qty')
    def _compute_discount_amount(self):
        for record in self:
            record.x_discount_amount = sum(((line.price_unit - line.price_reduce) * line.product_uom_qty) for line in record.order_line)

    @api.multi
    @api.depends('x_discount_amount', 'x_amount_untaxed')
    def _compute_discount_rate(self):
        for record in self:
            try:
                record.x_discount_rate = (1 - record.x_amount_untaxed / (record.x_amount_untaxed + record.x_discount_amount)) * 100
            except ZeroDivisionError:
                record.x_discount_rate = 0

    @api.model
    def _order_line_with_qty(self, record):
        return filter(lambda line: line.product_uom_qty > 0, record.order_line)

    @api.model
    def _order_line_with_qty_len(self, record):
        return float(len(self._order_line_with_qty(record=record)))
