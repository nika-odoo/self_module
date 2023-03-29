from odoo import models, fields


class Grocery(models.Model):
    _name = "gogrocery.admin"
    _description = "Go Grocery"

    name = fields.Char(required=True)
    shop_name = fields.Char(required=True)
    postcode = fields.Char()
    contact_num = fields.Float()
    email = fields.Char()
    address = fields.Text()
    description = fields.Text()
