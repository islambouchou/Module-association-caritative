# -*- coding: utf-8 -*-
{
    'name': "Association caritative",

    'summary': """Gestion Association caritative""",

    'description': """
        Gestion Association caritative module pour :
            - Gerer Campagne de dons  
            - Gerer Don 
            - Gerer Objets_donnés (constituant le don)
            - Gerer Donateur
            - Gerer Don Bénéficiaire
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
        'views/association.xml',
	    'reports.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
