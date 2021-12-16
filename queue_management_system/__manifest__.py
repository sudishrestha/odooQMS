# -*- coding: utf-8 -*-
{
    'name': "Queue Management System",

    'summary': """Manages queue of the hospital""",

    'description': """
       Manages queue of the hospital
    """,

    'author': "NepalEHR",
    'website': "http://www.nepalehr.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'queue',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["base","hr"],

    # always loaded
    'data': [
        'views/department_view.xml',
        'views/doctor_view.xml',
        'views/token_view.xml',
        'views/token_detail_view.xml',
        'views/qms_menu.xml'
    ],


    'installable': True,
    'auto_install': False,
    'application': True
}