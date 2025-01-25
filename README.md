# Objetivo

Diseñar un módulo en odoo para gestionar el inventario de vehículos utilizados en el transporte de fletes de cerdos y pollos vivos, las características deben incluir el registro y estado del vehículo.

## Estructura de modelos

**fletes.vehiculos**
- matricula: Char
- placas: Char
- tipo_vehiculo_id: Many2one(fletes.vehiculos.tipo)
- capacidad: Float
- carga_promedio: Float
- capacidad_restante: Float
- estado: Selection(disponible, mantenimiento, inactivo)
- kilometraje: Float
- fecha_ultimo_mantenimiento: Date

**operador**
- name: Char

**fletes.vehiculos.tipo**
- name: Char

**fletes.vehiculos.costo.tipo**
- name: Char

**fletes.vehiculos.incidente**
- fecha: Date
- descripcion: Text
- responsable: Many2one(operador)
- acciones_tomadas: Text

**fletes.vehiculos.asignacion_conductor**
- fecha_asignacion: Date
- conductor: Many2one(operador)
- fecha_finalizacion: Date
- kilometraje_inicial: Float
- kilometraje_final: Float

**fletes.vehiculos.costo**
- fecha: Date
- tipo_costo_id: Many2one(fletes.vehiculos.costo.tipo)
- monto: Float
- descripcion: Text