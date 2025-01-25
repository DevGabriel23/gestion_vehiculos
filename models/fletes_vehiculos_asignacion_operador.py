from odoo import models, fields, api
from odoo.exceptions import ValidationError

class fletes_vehiculos_asignacion_operador(models.Model):
    _name = 'fletes.vehiculos.asignacion.operador'
    
    fecha_asignacion = fields.Date(string='Fecha asignación', required=True)
    fecha_finalizacion = fields.Date(string='Fecha finalización',)
    kilometraje_inicial = fields.Float(string='Kilometraje inicial', default=0, required=True)
    kilometraje_final = fields.Float(string='Kilometraje final',)
    
    operador_id = fields.Many2one('fletes.vehiculos.operador', string='Conductor', domain=[('is_assigned', '=', False)])
    vehicle_assigned_id = fields.Many2one('fletes.vehiculos', string="Vehículo", required=True)
    
    @api.onchange('fecha_asignacion')
    def _onchange_fecha_asignacion_(self):
        for record in self:
            if not record.fecha_asignacion:
                return
            
            if record.fecha_asignacion < fields.Date.today():
                raise ValidationError('La fecha de asignación no puede ser anterior a hoy')
            
    @api.onchange('fecha_finalizacion')
    def _onchange_fecha_finalizacion(self):
        for record in self:
            if not record.fecha_asignacion:
                return
            
            if record.fecha_finalizacion > record.fecha_asignacion:
                raise ValidationError('La fecha de finalización no puede ser anterior a la fecha de asignación')