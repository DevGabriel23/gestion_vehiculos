from odoo import models, fields,api

class fletes_vehiculos_operador(models.Model):
    _name = 'fletes.vehiculos.operador'
    _description = 'Operador (conductores)'
    
    # SQL Constraints
    _sql_constraints = [
        ('unique_type_name', 'UNIQUE(name)', 'El nombre del operador debe ser único.'),
    ]
    
    name = fields.Char(required=True, string='Nombre')
    is_assigned = fields.Boolean(default=False, compute='', store=True)
    
    asignacion_ids = fields.One2many('fletes.vehiculos.asignacion.operador', 'operador_id')
    