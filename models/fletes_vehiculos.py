from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class fletes_vehiculos(models.Model):
    _name = 'fletes.vehiculos'
    _description = 'Vehiculos'
    
    _inherit = ['mail.thread']
    
    # SQL Constraints
    _sql_constraints = [
        ('matricula_unique', 'UNIQUE(matricula)', 'La matrícula debe ser única'),
        ('capacidad_positive', 'CHECK(capacidad > 0)', 'La capacidad debe ser positiva'),
        ('carga_promedio_positive', 'CHECK(carga_promedio > 0)', 'La carga promedio debe ser positiva'),
        ('kilometraje_positive', 'CHECK(kilometraje >= 0)', 'El kilometraje debe ser positivo'),
    ]
    
    matricula = fields.Char(string='Matrícula', required=True, tracking=True,)
    placas = fields.Char(string='Placas')
    capacidad = fields.Float(string='Capacidad (kg)', required=True)
    carga_promedio = fields.Float(string='Capacidad promedio (kg)', required=True)
    estado = fields.Selection(
        string='Estado',
        selection=[
            ('disponible', 'Disponible'), 
            ('mantenimiento', 'Mantenimiento'),
            ('inactivo', 'Inactivo')
        ],
        tracking=True,
    )
    
    # Computed fields
    capacidad_restante = fields.Float(string='Capacidad restante (kg)', compute='_compute_capacidad_restante')
    kilometraje = fields.Float(string='Kilometraje', compute='_compute_kilometraje',  default=0, required=True)
    fecha_ultimo_mantenimiento = fields.Date(string='Fecha de último mantenimiento', tracking=True,)
    
    # Relationships
    tipo_vehiculo_id = fields.Many2one('fletes.vehiculos.tipo', string='Tipo de vehículo', required=True)
    incidente_ids = fields.One2many('fletes.vehiculos.incidente', 'vehicle_id', tracking=True,)
    asignacion_ids = fields.One2many('fletes.vehiculos.asignacion.operador', 'vehicle_assigned_id', tracking=True,)
    costo_ids = fields.One2many('fletes.vehiculos.costo', 'vehicle_cost_id', tracking=True,)
    
    # Computed methods
    @api.depends('capacidad', 'carga_promedio')
    def _compute_capacidad_restante(self):
        for record in self:
            record.capacidad_restante = record.capacidad - record.carga_promedio
    
    @api.depends('asignacion_ids.fecha_finalizacion')
    def _compute_kilometraje(self):
        for record in self:
            record.kilometraje = 0
            if record.asignacion_ids:
                record.kilometraje = record.asignacion_ids[-1].kilometraje_final
    
    # OnChange methods
    @api.onchange('carga_promedio', 'capacidad')
    def _check_carga_promedio(self):
        for record in self:
            if record.carga_promedio > record.capacidad:
                raise ValidationError('La carga promedio debe ser menor que la capacidad máxima')