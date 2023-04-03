from odoo import models, fields


class GogroceryOrder(models.Model):
    _name = "gogrocery.order"
    _description = "Go Grocery Order"

    name = fields.Char(required=True)
    id = fields.Integer()
    status = fields.Selection(selection=[
        ('new','New'),
        ('processing', 'Processing'),
        ('shipping', 'Shipping'),
        ('delivered', 'Delivered')
    ])
    order_price = fields.Float()
