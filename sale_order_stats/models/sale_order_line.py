# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    x_purchase_price = fields.Float(string='Purchase price', digits_compute=dp.get_precision('Product Price'))
    x_cost_subtotal = fields.Float(string='Cost subtotal', compute='_compute_cost_subtotal', store=True, digits_compute=dp.get_precision('Product Price'))
    x_margin_amount = fields.Float(string='Margin amount', compute='_compute_margin_amount', store=True, digits_compute=dp.get_precision('Product Price'))
    x_margin_rate = fields.Float(string='Margin rate', compute='_compute_margin_rate', store=True, digits_compute=dp.get_precision('Product Price'))
    x_markup_rate = fields.Float(string='Markup rate', compute='_compute_markup_rate', store=True, digits_compute=dp.get_precision('Product Price'))

    @api.multi
    @api.depends('x_purchase_price', 'product_uom_qty')
    def _compute_cost_subtotal(self):
        for record in self:
            record.x_cost_subtotal = record.x_purchase_price * record.product_uom_qty

    @api.multi
    @api.depends('x_cost_subtotal', 'price_subtotal')
    def _compute_margin_amount(self):
        for record in self:
            record.x_margin_amount = record.price_subtotal - record.x_cost_subtotal

    @api.multi
    @api.depends('x_margin_amount', 'x_cost_subtotal')
    def _compute_margin_rate(self):
        for record in self:
            try:
                record.x_margin_rate = record.x_margin_amount / record.x_cost_subtotal * 100
            except ZeroDivisionError:
                record.x_margin_rate = 0

    @api.multi
    @api.depends('x_margin_amount', 'price_subtotal')
    def _compute_markup_rate(self):
        for record in self:
            try:
                record.x_markup_rate = record.x_margin_amount / record.price_subtotal * 100
            except ZeroDivisionError:
                record.x_markup_rate = 0

    @api.onchange('product_id')
    def _init_purchase_price(self):
        if not self.product_id:
            return

        if not self.order_id.pricelist_id or not self.product_uom:
            self.x_purchase_price = self.product_id.standard_price
            return

        purchase_price = self.product_id.standard_price
        company_currency = self.env.user.company_id.currency_id
        pricelist_currency = self.order_id.pricelist_id.currency_id

        if self.product_uom != self.product_id.uom_id:
            purchase_price = self.env['product.uom']._compute_price(self.product_id.uom_id.id, purchase_price, to_uom_id=self.product_uom.id)

        ctx = self.env.context.copy()
        ctx['date'] = self.order_id.date_order

        self.x_purchase_price = company_currency.with_context(ctx).compute(purchase_price, pricelist_currency, round=False)

