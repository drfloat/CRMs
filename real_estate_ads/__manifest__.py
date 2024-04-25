{
    "name":"Real Estate Ads",
    "version":"1.0",
    "website":"https//www.theodooguys.com",
    "author":"Miracle",
    "description":"""
        Real Estate module to show available properties
    """,
    "category":"",
    "depends":['base'],
    "data":[
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/menu_items.xml'
    ],
    "installable":True,
    "application":True,
    "license":"LGPL-3"
}