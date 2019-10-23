{
    'name': "Zynthian Inventory Customs",
    'version': '1.0',
    'category' : 'Website',
    'website' : 'http://www.zynthian.org',
    'summary': 'Inventory Customs',
    'description': """
        Inventory modifications in order to classify and controll better stock:
        - Kit Version: field to classify in witch version some product is used. It will appears in Inventory page.
        """,
    'author': 'mumaker',
    'depends': ['product'],
    'data': [
        'views/zynthian_product_kit_version.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}