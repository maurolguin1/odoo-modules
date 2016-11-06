# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp.osv import osv


class ProductMargin(osv.osv_memory):
    _inherit = 'product.margin'

    def action_open_window(self, cr, uid, ids, context=None):
        vals = super(ProductMargin, self).action_open_window(cr, uid, ids, context)

        vals.update({
            'domain': [('product_tmpl_id', 'in', context.get('active_ids', []))]
        })

        return vals
