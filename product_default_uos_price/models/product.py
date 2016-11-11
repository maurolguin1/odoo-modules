# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    uom_so_standard_price_uom = fields.Many2one(related='uom_so_id', readonly=True)
    uom_so_standard_price = fields.Float(
        string='Cost (UoS)',
        compute='_compute_uom_so_standard_price',
        inverse='_inverse_uom_so_standard_price',
        digits_compute=dp.get_precision('Product Price'),
        store=True,
    )

    uom_so_list_price_uom = fields.Many2one(related='uom_so_id', readonly=True)
    uom_so_list_price = fields.Float(
        string='Sale price (UoS)',
        compute='_compute_uom_so_list_price',
        inverse='_inverse_uom_so_list_price',
        digits_compute=dp.get_precision('Product Price'),
        store=True,
    )

    @api.multi
    @api.onchange('uom_so_standard_price')
    def _inverse_uom_so_standard_price(self):
        for record in self:
            if not record.uom_so_id or not record.uom_po_id or record.uom_so_id == record.uom_po_id:
                record.standard_price = record.uom_so_standard_price
            else:
                record.standard_price = record.uom_so_standard_price * self.env['product.uom']._compute_qty_obj(
                    from_unit=record.uom_po_id,
                    qty=1,
                    to_unit=record.uom_so_id,
                    round=False
                )

    @api.multi
    @api.depends('uom_so_id', 'uom_po_id', 'standard_price')
    def _compute_uom_so_standard_price(self):
        for record in self:
            if not record.uom_so_id or not record.uom_po_id or record.uom_so_id == record.uom_po_id:
                record.uom_so_standard_price = record.standard_price
            else:
                record.uom_so_standard_price = record.standard_price / self.env['product.uom']._compute_qty_obj(
                    from_unit=record.uom_po_id,
                    qty=1,
                    to_unit=record.uom_so_id,
                    round=False
                )

    @api.multi
    @api.onchange('uom_so_list_price')
    def _inverse_uom_so_list_price(self):
        for record in self:
            if not record.uom_so_id or not record.uom_po_id or record.uom_so_id == record.uom_po_id:
                record.list_price = record.uom_so_list_price
            else:
                record.list_price = record.uom_so_list_price * self.env['product.uom']._compute_qty_obj(
                    from_unit=record.uom_id,
                    qty=1,
                    to_unit=record.uom_so_id,
                    round=False
                )

    @api.multi
    @api.depends('uom_so_id', 'uom_id', 'list_price', 'lst_price')
    def _compute_uom_so_list_price(self):
        for record in self:
            if not record.uom_so_id or not record.uom_id or record.uom_so_id == record.uom_id:
                record.uom_so_list_price = record.list_price
            else:
                record.uom_so_list_price = record.list_price / self.env['product.uom']._compute_qty_obj(
                    from_unit=record.uom_id,
                    qty=1,
                    to_unit=record.uom_so_id,
                    round=False
                )
