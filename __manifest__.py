{
    'name': 'Gestión de vehículos',
    'version': '0.1',
    'description': "Módulo para la gestión de vehículos",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/fletes_vehiculos_view.xml',
        'views/fletes_vehiculos_menu.xml',
    ],
    'application': True,
    'installable': True,
}