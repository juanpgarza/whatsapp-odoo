from odoo import models, fields, api

class WhatsappTemplate(models.Model):
    _name = 'on.whatsapp.template'
    _description = 'Message default in Whatsapp'
    _order = 'sequence'

    sequence = fields.Integer(default=10)

    name = fields.Char(string="Nombre")
    template_message = fields.Text(string="Mensaje")
    category = fields.Selection([('other', 'Other')], default='other', string="Categoría")

    active = fields.Boolean(string="Archivada", default=True)

