from odoo import api, fields, models, _


class Employee(models.Model):
    _name = "employee.demo.ept"
    _description = "Employees"

    name = fields.Char(string="Employee Name", help="Name of Employee")
    department = fields.Char(string="Department Name", help="Name of Department")
    position = fields.Char(string="Employee Position", help="Position")
    salary = fields.Float(string="Employee Salary", default=0.0, help="Employee Salary")
    hiredate = fields.Date(string="Hire Date", help="Employee's Hiredate")
    gender = fields.Selection(selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')],
                              help="Employee Gender")
    job_type = fields.Selection(selection=[('Permanent', 'Permanent'), ('Ad Hoc', 'Ad Hoc')],
                                help="Employee Job Type")
