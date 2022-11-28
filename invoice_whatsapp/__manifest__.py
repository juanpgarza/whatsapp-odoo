# Copyright 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Customer invoice whatsapp integrations",
    "summary": "Integrate whatsapp with customer invoice",
    "version": "15.0.1.0.0",
    "category": "Social",
    "website": "https://github.com/juanpgarza/whatsapp-odoo",
    "author": "juanpgarza",
    "license": "AGPL-3",
    "depends": [
            "base",
            "account",
            "base_whatsapp",
        ],
    "data": [
        "data/invoice_whatsapp.xml",
        'views/account_move_view.xml',
        "wizards/wizard_account_invoice_view.xml",
        'security/ir.model.access.csv',
        ],
    "development_status": "Production/Stable",
    "installable": True,
}
