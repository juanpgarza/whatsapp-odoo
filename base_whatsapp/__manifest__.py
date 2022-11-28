# Copyright 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Base Whatsapp",
    "summary": "",
    "version": "15.0.1.0.0",
    "category": "Social",
    "website": "https://github.com/juanpgarza/whatsapp-odoo",
    "author": "openNova",
    "license": "AGPL-3",
    "depends": [
            "base",
        ],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/on_whatsapp_template_view.xml',
        ],
    "installable": True,
}
