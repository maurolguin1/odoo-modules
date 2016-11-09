# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    uom_so_id = fields.Many2one(string='Default Sale Unit', comodel_name='product.uom', required=True)

    @api.constrains('uom_id', 'uom_so_id')
    def _check_uom_so(self):
        for record in self:
            if record.uom_id.category_id.id != record.uom_so_id.category_id.id:
                raise ValidationError('Error: The default Unit of Measure and the sale Unit of Measure must be in the same category.')

    def onchange_uom(self, cursor, user, ids, uom_id, uom_po_id):
        vals = super(ProductTemplate, self).onchange_uom(cursor, user, ids, uom_id, uom_po_id)

        if uom_id and 'value' in vals:
            vals['value']['uom_so_id'] = uom_id

        return vals
