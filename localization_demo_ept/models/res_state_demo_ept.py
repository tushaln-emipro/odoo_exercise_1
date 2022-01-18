from odoo import api, fields, models, _


class State(models.Model):
    _name = "res.state.demo.ept"
    _description = "State"

    state = fields.Char(string="State", help="State Name")
    short_code = fields.Char(string="Short Code", help="State short code")
    country = fields.Char(string="Country", help="Country of state", copy=False)
    active = fields.Boolean(string="Active", help="State Is Active or Not")
