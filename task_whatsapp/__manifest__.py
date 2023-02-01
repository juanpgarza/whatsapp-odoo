# Copyright 2023 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Project Task whatsapp integrations",
    "summary": "Integrate whatsapp with project task operations",
    "version": "15.0.1.0.0",
    "category": "Social",
    "website": "https://github.com/juanpgarza/whatsapp-odoo",
    "author": "juanpgarza",
    "license": "AGPL-3",
    "depends": [
            "base",
            "project",
            "base_whatsapp",
        ],
    "data": [
        "data/task_whatsapp.xml",
        'views/project_task_view.xml',
        "wizards/wizard_project_task_view.xml",
        'security/ir.model.access.csv',
        ],
    "development_status": "Production/Stable",
    "installable": True,
}
