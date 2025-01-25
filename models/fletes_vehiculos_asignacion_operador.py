from odoo import models, fields, api
from odoo.exceptions import ValidationError

class fletes_vehiculos_asignacion_operador(models.Model):
    _name = 'fletes.vehiculos.asignacion.operador'
    
    fecha_asignacion = fields.Date(string='Fecha asignación', required=True)
    fecha_finalizacion = fields.Date(string='Fecha finalización',)
    kilometraje_inicial = fields.Float(string='Kilometraje inicial', default=0, required=True)
    kilometraje_final = fields.Float(string='Kilometraje final',)
    
    operador_id = fields.Many2one('fletes.vehiculos.operador', string='Conductor', domain=[('is_assigned', '=', False)], required=True)
    vehicle_assigned_id = fields.Many2one('fletes.vehiculos', string="Vehículo", required=True)
    
    @api.onchange('kilometraje_final', 'kilometraje_inicial')
    def _onchange_kilometraje_final(self):
        for record in self:
            if record.kilometraje_final and record.kilometraje_inicial > record.kilometraje_final:
                raise ValidationError("El kilometraje inicial no puede ser mayor que el kilometraje final")
    
    @api.constrains('kilometraje_inicial', 'kilometraje_final')
    def _constrains_kilometraje_inicial(self):
        for record in self:
            last_kilometraje_inicial = record.vehicle_assigned_id.asignacion_ids[-1].kilometraje_inicial
            if record.kilometraje_final < last_kilometraje_inicial:
                raise ValidationError("El kilometraje final no puede ser menor que el ultimo kilometraje inicial")
    
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
            
            if record.fecha_asignacion > record.fecha_finalizacion:
                raise ValidationError('La fecha de finalización no puede ser anterior a la fecha de asignación')
    
    @api.constrains('kilometraje_final', 'fecha_finalizacion')
    def _constrains_kilometraje_final(self):
        for record in self:
            if not record.fecha_finalizacion and record.kilometraje_final:
                raise ValidationError('No se puede establecer kilometraje final sin una fecha de finalización')
    
    @api.constrains('fecha_finalizacion')
    def _constrains_fecha_finalizacion(self):
        for record in self:
            if record.fecha_finalizacion:
                record.operador_id.is_assigned = False

    @api.constrains('fecha_asignacion')
    def _constrains_fecha_finalizacion(self):
        for record in self:
            if record.fecha_asignacion and not record.fecha_finalizacion:
                record.operador_id.is_assigned = True
