from odoo import models,fields

class GroceryProductType(models.Model):
    _name = "gogrocery.product.type"
    _description = "grocery application"

    name = fields.Char(required=True)
   
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
      ]