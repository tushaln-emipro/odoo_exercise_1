from odoo import api, fields, models, _


class DemoEpt2(models.Model):
    _name = "res.partner.demo.ept2"
    _description = "This ept2 module of Requirement - 1"

    name = fields.Char(string="Name", help="Customer Name")
    email = fields.Char(string="Email", help="Customer Email")
    street1 = fields.Char(string="Street 1", help="Customer Street 1")
    street2 = fields.Char(string="Street 2", help="Customer Street 2")
    city = fields.Char(string="City", help="Customer City")
    state = fields.Char(string="State", help="Customer State")
    zip_code = fields.Char(string="Zip Code", help="Customer Zip Code")
    country = fields.Char(string="Country", help="Customer Country")
    birthdate = fields.Date(string="BirthDate", help="Customer Birthdate")
    age = fields.Integer(string="Age", help="Customer Age")
    weight = fields.Float(string="Weight", help="Customer Weight")
    description = fields.Text(string="Description", help="If any Description")
    gender = fields.Selection(selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')],
                              help="Customer Gender")
    details = fields.Html(string="Details", help="Customer Full Details")
    is_spectacles = fields.Boolean(string="Is Spectacles", help="Customer Is Spectacles")
    photo = fields.Image(string="Photo", help="Customer Photo")
