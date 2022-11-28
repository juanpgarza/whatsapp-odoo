import logging
import urllib
import html2text
from odoo import http, models, fields, api, tools, _
from odoo.http import request

_logger = logging.getLogger(__name__)

class ConvertHtmlText(object):

    def convert_html_to_text(result_txt):
        capt = b'%s' % (result_txt)
        convert_byte_to_str = capt.decode('utf-8')
        return html2text.html2text(convert_byte_to_str)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    send_whatsapp = fields.Selection([
        ('without_sending', 'without sending'),
        ('sent', 'sent'), ('not_sent', 'no sent'),
        ], default='without_sending')

    def send_whatsapp_step(self):

        return {'type': 'ir.actions.act_window',
                'name': _('Send Whatsapp'),
                'res_model': 'send.whatsapp.sale',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {
                            'default_partner_id': self.partner_id.id,
                            'format_invisible': True
                            },
                }

    def url_link_sale(self):

        dominio = http.request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        url_preview = self.get_portal_url()
        format_url = '{}{}'.format(dominio, url_preview)

        return format_url

    def _action_whatsapp_confirmed(self, message=None):
        self.ensure_one()
        lang = self.env.context.get('lang')

        ctx = {
            'default_model': 'sale.order',
            'default_res_id': self.ids[0],
            'default_composition_mode': 'comment',
            'mark_so_as_sent': False,
            'mark_whatsapp_sent': True,
            'custom_layout': False,
            'proforma': self.env.context.get('proforma', False),
            'force_email': False,
            }

        subtype_id = self.env['ir.model.data']._xmlid_to_res_id('mail_mt_note')
        self.with_context(ctx).message_post(attachment_ids=[], body=message, canned_response_ids=[],
                                            message_type='notification', partner_ids=[], subtype_xmlid=None,
                                            subtype_id=subtype_id)

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):

        res = super(SaleOrder, self.with_context(mail_post_autofollow=True)).message_post(**kwargs)
        if self.env.context.get('mark_whatsapp_sent'):
           pass

        return res
