from odoo import models, fields


class GroceryProduct(models.Model):
    _name = "gogrocery.product"
    _description = "Go Grocery Product"
    _rec_name = "product_name"

    product_name = fields.Char(required=True)
    shop_ids = fields.Many2many("gogrocery.admin",  required=True)
    price = fields.Float()
    category_ids = fields.Many2one("gogrocery.product.type", string = "Product Type")
    discount = fields.Boolean()
    discounted_price = fields.Float()
    quantity = fields.Float()
    description = fields.Text()

   
