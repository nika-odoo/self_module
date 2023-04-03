{
    'name': "Go Grocery",
    'version': '1.0',
    'depends': ['base'],
    'author': "Nikhil Kajavadra",
    'category': 'Category',
    'description': """
    Description text 
    """,

    'depends' : ['product'],

    'data': [
        'security/ir.model.access.csv',
        'view/gogrocery_admin_view.xml',
        # 'view/gogrocery_product_view.xml',
        'view/product.xml',
        'view/gogrocery_order_view.xml',
        'view/gogrocery_menus.xml'
    ],

    'demo': [
        



    ],
    'application': True,
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
