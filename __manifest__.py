# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'author': 'TsaRiadh',
    'version': '1.0.0',
    'category': '',
    'sequence': -100,    #to show it in the first place
    'summary': 'Hospital management system',
    'description': """Hospital management system""",
    'depends': ['base', 'mail' ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_appointment_views.xml',
        'views/patient.xml',
        'views/kids.xml',
        'views/patient_gender.xml',
        'views/appointment.xml',
        'views/doctor.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,    # able to search it with apps filter
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3'
}
