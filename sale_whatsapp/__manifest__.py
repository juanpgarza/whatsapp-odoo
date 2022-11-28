# Copyright 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sale whatsapp integrations",
    "summary": "Integrate whatsapp with Sale App",
    "version": "15.0.1.0.0",
    "category": "Social",
    "website": "https://github.com/juanpgarza/whatsapp-odoo",
    "author": "juanpgarza",
    "license": "AGPL-3",
    "depends": [
            "base",
            "sale",
            "base_whatsapp",
        ],
    "data": [
        "data/sale_whatsapp.xml",
        'views/sale_order_view.xml',
        "wizards/wizard_sale_order_view.xml",
        'security/ir.model.access.csv',
        ],
    "development_status": "Production/Stable",
    "installable": True,
}
