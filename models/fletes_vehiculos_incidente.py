from odoo import models, fields, api

class fletes_vehiculos_incidente(models.Model):
    _name = 'fletes.vehiculos.incidente'
    _description = 'Incidentes ocurridos durante el uso de un vehículo'
    
    fecha = fields.Date(string='Fecha del incidente', required=True)
    descripcion = fields.Text(string='Descripcion')
    acciones_tomadas = fields.Text(string='Acciones tomadas')
    
    # Relationship
    responsable = fields.Many2one('fletes.vehiculos.operador', string="Responsable", required=True)
    vehicle_id = fields.Many2one('fletes.vehiculos', string="Vehículo", required=True)