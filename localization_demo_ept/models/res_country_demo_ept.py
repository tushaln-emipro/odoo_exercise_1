from odoo import api, fields, models, _

class Country(models.Model):

    _name = "res.country.demo.ept"
    _description = "Country"

    country = fields.Char(string="Country", help="Country Name")
    short_code = fields.Char(string="Short Code", help="Country Short Code")
    active = fields.Boolean(string="Active", help="Country Is Active or Not")
