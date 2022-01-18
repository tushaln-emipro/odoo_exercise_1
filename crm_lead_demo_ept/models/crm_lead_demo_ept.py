from odoo import api, fields, models, _


class Employee(models.Model):
    _name = "crm.lead.demo.ept"
    _description = "CRM Lead"

    customer_name = fields.Char(string="Customer Name", help="Name of Customer", required=True)
    customer_email = fields.Char(string="Customer Email", help="Customer's Email", required=True)
    customer_phone = fields.Char(string="Customer Phone", help="Customer's Phone", required=True)
    expected_revenue = fields.Float(string="Expected revenue", default=0.0, help="Expected revenue ")
    salesperson = fields.Char(string="Sales Person", help="Sales Person", required=True)
    salesteam = fields.Char(string="Sales Team", help="Sales Team")
    campaign = fields.Char(string="Campaign", help="Campaign")
    channel = fields.Selection(string="Channel",
                               selection=[('Facebook', 'Facebook'), ('WhatsApp', 'WhatsApp'), ('Email', 'Email'),
                                          ('Newspaper', 'Newspaper'), ('Television', 'Television'),
                                          ('Phone Call', 'Phone Call'), ('SMS', 'SMS'), ('Google Ads', 'Google Ads')],
                               help="Channel", required=True)
    state = fields.Selection(string="State",
                             selection=[('New', 'New'), ('Qualified', 'Qualified'), ('Proposition', 'Proposition'),
                                        ('Won', 'Won'), ('Lost', 'Lost')], help="State", default="New")
    follow_up_date = fields.Date(string="Next Follow Up Date", help="Next Follow Up Date", required=True)
    won_date = fields.Date(string="Won Date", help="Won Date")
    lost_reason = fields.Char(string="Lost reason", help="Lost reason")

