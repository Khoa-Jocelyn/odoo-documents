{
    'name': "Hospital Management",
    'name_vi_VN': "Quản lý bệnh viên",
    'summary': """Hospital Management Software""",
    'summary_vi_VN': """Phần mềm quản lý bệnh viện""",
    'sequence': -100,
    'description': """Hospital Management Software""",
    'description_vi_VN': """Phần mềm quản lý bệnh viện""",
    'author': "Viindoo",
    'website': "https://viindoo.com",
    'support': "apps.support@viindoo.com",
    'category': 'Productivity',
    'version': '1.0',
    'depends': [
        'base'
    ],
    'data': [
        "views/patient_views.xml",
        # "security/ir.model.access.csv",
    ],
    # 'images' : [
    #     'static/description/icon.png'
    # ],
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'price': 99.9,
    'currency': 'EUR',
    'license': 'LGPL-3',
}
