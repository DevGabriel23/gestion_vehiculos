from odoo import models, fields,api

class fletes_vehiculos_tipo(models.Model):
    _name = 'fletes.vehiculos.tipo'
    _description = 'Tipo de vehículos'
    
    # SQL Constraints
    _sql_constraints = [
        ('unique_type_name', 'UNIQUE(name)', 'El nombre del tipo de vehículo debe ser único.'),
    ]
    
    name = fields.Char(required=True)
    