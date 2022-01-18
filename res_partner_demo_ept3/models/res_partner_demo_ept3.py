from odoo import api, fields, models, _


class DemoEpt3(models.Model):
    _name = "res.partner.demo.ept3"
    _description = "This ept3 module of Requirement - 1"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
