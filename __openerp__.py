# -*- coding: utf-8 -*-
{
    'name': "Livestock",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Autana's Development Team",
    'website': "http://www.autanact.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Development',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'stock',
    ],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'templates.xml',
        'views/livestock_embryo_view.xml',
        'views/livestock_straw_view.xml',
        'views/livestock_thermo_view.xml',
        'views/livestock_animal_view.xml',
        'views/livestock_corral_view.xml',
        'views/livestock_farm_view.xml',
        'views/livestock_event_view.xml',
        'views/livestock_disease_view.xml',
        'views/livestock_sanitary_protocol_view.xml',
        'views/livestock_weighing_view.xml',
        'views/livestock_nutrition_view.xml',
        'views/livestock_specie_animal_view.xml',
        'views/livestock_race_animal_view.xml',
        'views/livestock_color_animal_view.xml',
        'views/livestock_status_animal_view.xml',
        'views/livestock_thermo_event_view.xml',
        'livestock_report.xml',
        'reports/offspring_view.xml',
        'reports/fattening_view.xml',
        'reports/thermo_view.xml',
        'reports/corral_view.xml',
        'wizard/livestock_offspring_wizard_view.xml',
        'wizard/livestock_fattening_wizard_view.xml',
        'wizard/livestock_thermo_wizard_view.xml',
        'wizard/livestock_corral_wizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
