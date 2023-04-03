from odoo import models,fields

class GroceryProductType(models.Model):
    _name = "gogrocery.product.type"
    _description = "grocery application"

    name = fields.Selection(required=True, selection=[
            ('food', 'Food'),
            ('Dairy', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')
        ], default="new"
    )
   
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
      ]