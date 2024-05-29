# -*- coding: utf-8 -*-
from odoo import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    is_material_issue = fields.Boolean(string="Material request",
                                       help="Enable this field to add issue "
                                            "product.",
                                       default=False)
    issue_product_id = fields.Many2one(comodel_name="product.product",
                                       help="Once selected, the move-line "
                                            "products will be affected with "
                                            "issue product expense account.",
                                       string="Issue Product")

    def button_validate(self):
        """
        Check if material issue is enabled and
        issue product has expense account.
        """
        if self.is_material_issue and \
                self.issue_product_id.property_account_expense_id:
            for move in self.move_ids:
                move.product_id.property_account_expense_id = \
                    self.issue_product_id.property_account_expense_id
        return super().button_validate()
