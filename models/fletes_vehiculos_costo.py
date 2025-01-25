from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class fletes_vehiculos_costo(models.Model):
    _name = 'fletes.vehiculos.costo'
    
    _sql_constraints = [
        ('monto_positive', 'CHECK(monto > 0)', 'El monto debe ser positivo'),
    ]
    
    fecha = fields.Date(string='Fecha')
    monto = fields.Float(string='Monto')
    descripcion = fields.Text(string='Descripcion')
    
    costo_id = fields.Many2one('fletes.vehiculos.costo.tipo', string='Tipo de costo')
    vehicle_cost_id = fields.Many2one('fletes.vehiculos', string="Vehículo", required=True)
    
    @api.onchange('monto')
    def _onchange_monto(self):
        for record in self:
            if not record.monto:
                return
            
            if record.monto <= 0:
                raise UserError("El monto debe ser mayor a 0")
    
    @api.onchange('fecha')
    def _onchange_fecha_(self):
        for record in self:
            if not record.fecha:
                return
            
            if record.fecha < fields.Date.today():
                raise ValidationError('La fecha no puede ser anterior a hoy')