# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_disable_picking = fields.Boolean(default=True)

    def action_create_delivery(self):
        """
        enable picking and launch procurement.
        """
        self.is_disable_picking = False
        self.order_line._action_launch_stock_rule()
        self._action_confirm()


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _action_launch_stock_rule(self, previous_product_uom_qty=False):
        """
        Inherited to prevent creation of procurement.
        :param previous_product_uom_qty:
        :return:
        """
        if self.order_id.is_disable_picking:
            return True
        else:
            return super()._action_launch_stock_rule(
                previous_product_uom_qty=previous_product_uom_qty)
