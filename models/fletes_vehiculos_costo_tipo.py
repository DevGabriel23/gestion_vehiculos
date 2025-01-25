from odoo import models, fields,api

class fletes_vehiculos_costo_tipo(models.Model):
    _name = 'fletes.vehiculos.costo.tipo'
    _description = 'Tipos de costo'
    
    # SQL Constraints
    _sql_constraints = [
        ('unique_type_name', 'UNIQUE(name)', 'El nombre del tipo de costo debe ser único.'),
    ]
    
    name = fields.Char(required=True, string="Nombre")
    