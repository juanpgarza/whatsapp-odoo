from odoo import models, fields, api

class WhatsappTemplate(models.Model):
    _inherit = 'on.whatsapp.template'

    category = fields.Selection(selection_add=[('task', 'Tareas')])
