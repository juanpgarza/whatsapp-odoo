# Copyright 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Partner whatsapp integrations",
    "summary": "Integrate whatsapp with partner",
    "version": "15.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "https://github.com/juanpgarza/whatsapp-odoo",
    "author": "juanpgarza",
    "license": "AGPL-3",
    "depends": [
        "base",
            "contacts",
            "jitsi_meet",
            "base_whatsapp",
        ],
    "data": [
        "data/partner_whatsapp.xml",
        'views/res_partner_view.xml',
        "wizards/wizard_res_partner_view.xml",
        'security/ir.model.access.csv',
        ],
    "development_status": "Production/Stable",
    "installable": True,
}
