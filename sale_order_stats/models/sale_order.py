# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_amount_untaxed = fields.Monetary(string='Turnover', related='amount_untaxed')
    margin = fields.Float(string='Margin amount')

    x_margin_rate = fields.Float(string='Margin rate', compute='_compute_margin_rate', store=True)
    x_markup_rate = fields.Float(string='Markup rate', compute='_compute_markup_rate', store=True)

    @api.multi
    @api.depends('margin', 'order_line.purchase_price')
    def _compute_margin_rate(self):
        for record in self:
            try:
                record.x_margin_rate = record.margin / sum(map((lambda line: line.purchase_price * line.product_uom_qty), record.order_line)) * 100
            except ZeroDivisionError:
                record.x_margin_rate = 0

    @api.multi
    @api.depends('margin', 'order_line.price_subtotal')
    def _compute_markup_rate(self):
        for record in self:
            try:
                record.x_markup_rate = record.margin / sum(map((lambda line: line.price_subtotal), record.order_line)) * 100
            except ZeroDivisionError:
                record.x_markup_rate = 0

