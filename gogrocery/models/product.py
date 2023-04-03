from odoo import models, fields

class Product(models.Model):
    # _name="in.product.product"
    _inherit = "product.product"

    shop_ids = fields.Many2many("gogrocery.admin",  required=True)