# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields


class SaleReport(models.Model):
    _inherit = 'sale.report'

    x_margin_rate = fields.Float(string='Margin rate', readonly=True, group_operator='avg')
    x_markup_rate = fields.Float(string='Markup rate', readonly=True, group_operator='avg')

    def _select(self):
        sql = ''
        sql += ', AVG(s.x_margin_rate) AS x_margin_rate'
        sql += ', AVG(s.x_markup_rate) AS x_markup_rate'
        
        return super(SaleReport, self)._select() + sql
