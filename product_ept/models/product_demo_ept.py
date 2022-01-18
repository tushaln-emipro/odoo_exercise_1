from odoo import api, fields, models, _


class Product(models.Model):
    _name = "product.demo.ept"
    _description = "Products"

    name = fields.Char(string="Product Name", help="Name of product")
    sku = fields.Char(string="SKU", help="Product's SKU")
    barcode = fields.Char(string="Barcode", help="Barcode of the product ")
    be_sold = fields.Boolean(string="Can this product be sold", help="Can this product be sold")
    product_type = fields.Selection(
        selection=[('Storable', 'Storable'), ('Consumable', 'Consumable'), ('Service', 'Service')], help="Product Type")
    sale_price = fields.Float(string="Sale Price", default=0.0, help="Product Sale price")
    cost_price = fields.Float(string="Cost Price", default=0.0, help="Product Cost price")
    active = fields.Boolean(string="Active", help="Can this be Active")
    warehouse = fields.Char(string="Warehouse", help="Warehouse")
    image = fields.Image(string="Product Image", help="Product Photo")
    description = fields.Html(string="Website Description", help="Website Description")
    internal_note = fields.Text(string="Internal Note", help="Internal Notes")
