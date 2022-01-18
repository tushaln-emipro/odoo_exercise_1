# -*- coding: utf-8 -*-

{
    'name': 'Localization Demo',
    'version': '1.0',
    'category': 'Localization_Demo',
    'summary': 'Localization_Demo',
    'description': 'Localization Demo',
    'depends': ['sales_team'],
    'data': [],
    'data': ['security/ir.model.access.csv', 'views/view_country.xml', 'views/view_state.xml', 'views/view_city.xml'],
    'demo': ['data/view_country_demo_data.xml','data/view_state_demo_data.xml'],
    'installable': True,
    'auto_install': False
}
