# Copyright 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Stock Picking whatsapp integrations",
    "summary": "Integrate whatsapp with stock picking operations",
    "version": "15.0.1.0.0",
    "category": "Social",
    "website": "https://github.com/juanpgarza/whatsapp-odoo",
    "author": "juanpgarza",
    "license": "AGPL-3",
    "depends": [
            "base",
            "stock",
            "base_whatsapp",
            "stock_voucher",
        ],
    "data": [
        "data/picking_whatsapp.xml",
        'views/stock_picking_view.xml',
        "wizards/wizard_stock_picking_view.xml",
        'security/ir.model.access.csv',
        ],
    "development_status": "Production/Stable",
    "installable": True,
}
