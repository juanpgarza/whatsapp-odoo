from odoo import models, fields, api

# la plantilla de los mensajes
class WhatsappTemplate(models.Model):
    _inherit = 'on.whatsapp.template'

    category = fields.Selection(selection_add=[('partner', 'Contactos')])
