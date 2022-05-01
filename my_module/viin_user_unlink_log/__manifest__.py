{
    'name': "User Document Unlink Logs",
    'name_vi_VN': "Nhật ký xóa tài liệu của người dùng",

    'summary': """
Log user document unlink action""",

    'summary_vi_VN': """
Ghi lại nhật ký xóa tài liệu của người dùng
        """,

    'description': """
What it does
============
1. Allow to log user unlink document for all types of document. For example,
   
   * Lead
   * Sale Order
   * Invoice
   * etc

2. All log can be access from menu Setting/Technical/User Unlink/Log

Editions Supported
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Ứng dụng này làm gì
===================
1. Cho phép ghi lại nhật ký xóa tài liệu cho người dùng đối với mọi loại tài liệu trên hệ thống. Ví dụ,

   * Cơ hội
   * Đơn bán
   * Hóa đơn,
   * v.v.

2. Có thể truy cập tất cả lịch sử từ menu Thiết lập/Kỹ thuật/Phân công công việc/Lịch sử

Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

    """,

    'author': "Viindoo",
    'website': "https://viindoo.com",
    'live_test_url': "https://v14demo-int.viindoo.com",
    'live_test_url_vi_VN': "https://v14demo-vn.viindoo.com",
    'support': "apps.support@viindoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/tvtma/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources/Tracking',
    'version': '0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/module_security.xml',
        'security/ir.model.access.csv',
        'views/ir_model_views.xml',
        'views/user_unlink_log_views.xml',
        # 'views/res_users_views.xml',
    ],

    'images': [
        # 'static/description/main_screenshot.png'
        ],
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'application': False,
    'auto_install': True,
    'price': 99.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}
