# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from openerp import models, fields


class SaleReport(models.Model):
    _inherit = 'sale.report'

    discount_amount = fields.Float(string='Discount amount', readonly=True, group_operator='sum')
    discount_rate = fields.Float(string='Discount rate', readonly=True, group_operator='avg')
    margin_amount = fields.Float(string='Margin amount', readonly=True, group_operator='sum')
    margin_rate = fields.Float(string='Margin rate', readonly=True, group_operator='avg')
    markup_rate = fields.Float(string='Markup rate', readonly=True, group_operator='avg')

    def _select(self):
        sql = ''
        sql += ', SUM(l.discount_amount) AS discount_amount'
        sql += ', AVG(l.discount_rate) AS discount_rate'

        sql += ', SUM(l.margin_amount) AS margin_amount'
        sql += ', AVG(l.margin_rate) AS margin_rate'

        sql += ', AVG(l.markup_rate) AS markup_rate'
        
        return super(SaleReport, self)._select() + sql