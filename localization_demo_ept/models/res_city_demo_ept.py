from odoo import api, fields, models, _


class City(models.Model):
    _name = "res.city.demo.ept"
    _description = "City"

    city = fields.Char(string="City", help="City Name")
    state = fields.Char(string="State", help="State Of Country", copy=False)
    active = fields.Boolean(string="Active", help="Citys Is Active or Not")
