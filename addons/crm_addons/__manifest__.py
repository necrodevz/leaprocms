# -*- coding: utf-8 -*-
{
    'name': "Leapro : CRM Addons",

    'summary': """Adds Leapro CRM UI""",

    'description': """
        Adds UI elements to CRM:
            - Add Technichian to Activities
    """,

    'author': "Devroy Blake <info@dkblake.com>",
    'website': "https://www.dkblake.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Leapro',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'sale','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/crm_activity_log'
    ],
    # only loaded in demonstration mode
    'demo': [
        'data/demo.xml',
    ],
}