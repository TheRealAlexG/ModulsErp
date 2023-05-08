from odoo import models, fields     
class plane_vol(models.Model): 
    _name = 'plane.vol' 
    codi = fields.Integer('Codi', required=True) 
    passatgers = fields.Integer('Passatgers', required=True)     
    dataSortida = fields.Datetime('Data Sortida')
    dataArrivada = fields.Datetime('Data Arrivada')
