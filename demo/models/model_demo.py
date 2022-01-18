from odoo import api, fields, models, _
class Demo(models.Model):

    _name = 'res.demo'
    _description = "My first demo"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    phone_no = fields.Char(string="Phone No.")