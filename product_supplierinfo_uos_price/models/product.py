# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp


class ProductSupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'

    product_uom_po_id = fields.Many2one(related='product_tmpl_id.uom_po_id', readonly=True)
    product_uom_so_id = fields.Many2one(related='product_tmpl_id.uom_so_id', readonly=True)
    product_uom_equal = fields.Boolean(compute='_compute_product_uom_equal')

    uom_so_price = fields.Float(
        string='Price (UoS)',
        compute='_compute_uom_so_price',
        inverse='_inverse_uom_so_price',
        digits_compute=dp.get_precision('Product Price'),
        store=True,
    )

    @api.multi
    def _inverse_uom_so_price(self):
        for record in self:
            if not record.product_uom_so_id or not record.product_uom_po_id or record.product_uom_so_id == record.product_uom_po_id:
                record.price = record.uom_so_price
            else:
                record.price = self.env['product.uom']._compute_price(
                    record.product_uom_so_id.id,
                    record.uom_so_price,
                    record.product_uom_po_id.id
                )

    @api.multi
    @api.depends('product_uom_so_id', 'product_uom_po_id', 'price')
    def _compute_uom_so_price(self):
        for record in self:
            if not record.product_uom_so_id or not record.product_uom_po_id or record.product_uom_so_id == record.product_uom_po_id:
                record.uom_so_price = record.price
            else:
                record.uom_so_price = self.env['product.uom']._compute_price(
                    record.product_uom_po_id.id,
                    record.price,
                    record.product_uom_so_id.id
                )

    @api.multi
    @api.depends('product_uom_so_id', 'product_uom_po_id')
    def _compute_product_uom_equal(self):
        for record in self:
            record.product_uom_equal = record.product_uom_so_id and record.product_uom_po_id and record.product_uom_so_id == record.product_uom_po_id
