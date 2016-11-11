# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    purchase_price = fields.Float(string='Purchase price', digits_compute=dp.get_precision('Product Price'))
    cost_subtotal = fields.Float(string='Cost subtotal', compute='_compute_cost_subtotal', store=True, digits_compute=dp.get_precision('Product Price'))
    margin_amount = fields.Float(string='Margin amount', compute='_compute_margin_amount', store=True, digits_compute=dp.get_precision('Product Price'))
    margin_rate = fields.Float(string='Margin rate', compute='_compute_margin_rate', store=True, digits_compute=dp.get_precision('Product Price'))
    markup_rate = fields.Float(string='Markup rate', compute='_compute_markup_rate', store=True, digits_compute=dp.get_precision('Product Price'))
    discount_amount = fields.Float(string='Discount amount', compute='_compute_discount_amount', store=True, digits_compute=dp.get_precision('Product Price'))
    discount_rate = fields.Float(string='Discount rate', compute='_compute_discount_rate', store=True, digits_compute=dp.get_precision('Product Price'))

    @api.multi
    @api.depends('purchase_price', 'product_uom_qty')
    def _compute_cost_subtotal(self):
        for record in self:
            record.cost_subtotal = record.purchase_price * record.product_uom_qty

    @api.multi
    @api.depends('cost_subtotal', 'price_subtotal')
    def _compute_margin_amount(self):
        for record in self:
            record.margin_amount = record.price_subtotal - record.cost_subtotal

    @api.multi
    @api.depends('margin_amount', 'cost_subtotal')
    def _compute_margin_rate(self):
        for record in self:
            try:
                record.margin_rate = record.margin_amount / record.cost_subtotal * 100
            except ZeroDivisionError:
                record.margin_rate = 0

    @api.multi
    @api.depends('margin_amount', 'price_subtotal')
    def _compute_markup_rate(self):
        for record in self:
            try:
                record.markup_rate = record.margin_amount / record.price_subtotal * 100
            except ZeroDivisionError:
                record.markup_rate = 0

    @api.multi
    @api.depends('price_unit', 'price_reduce', 'product_uom_qty')
    def _compute_discount_amount(self):
        for record in self:
            record.discount_amount = (record.price_unit - record.price_reduce) * record.product_uom_qty

    @api.multi
    @api.depends('discount_amount', 'price_subtotal')
    def _compute_discount_rate(self):
        for record in self:
            try:
                record.discount_rate = (1 - record.price_subtotal / (record.price_subtotal + record.discount_amount)) * 100
            except ZeroDivisionError:
                record.discount_rate = 0

    @api.onchange('product_id', 'product_uom')
    def _init_purchase_price(self):

        if not self.product_id:
            return

        if not self.order_id.pricelist_id or not self.product_uom:
            self.purchase_price = self.product_id.standard_price
            return

        purchase_price = self.product_id.standard_price
        company_currency = self.env.user.company_id.currency_id
        pricelist_currency = self.order_id.pricelist_id.currency_id

        purchase_uom = self.product_id.uom_po_id
        order_line_uom = self.product_uom

        if order_line_uom != purchase_uom:
            purchase_price = self.env['product.uom']._compute_price(purchase_uom.id, purchase_price, order_line_uom.id)

        ctx = self.env.context.copy()
        ctx['date'] = self.order_id.date_order

        self.purchase_price = company_currency.with_context(ctx).compute(purchase_price, pricelist_currency, round=False)
