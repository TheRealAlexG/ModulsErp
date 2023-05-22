from odoo import models, fields     
class plane_vol(models.Model): 
    _name = 'plane.vol' 
    codi = fields.Integer('Codi', required=True) 
    passatgers = fields.Integer('Passatgers', required=True)     
    dataSortida = fields.Datetime('Data Sortida')
    dataArrivada = fields.Datetime('Data Arrivada')
    avio_id = fields.Many2one('plane.avio',string = 'avio')
    pilot_id = fields.Many2one('plane.pilot',string = 'pilot')
    aeroportOrigen_id = fields.Many2one('plane.aeroport',string = 'Aeroport Origen')
    aeroportDesti_id = fields.Many2one('plane.aeroport',string = 'Aeroport Desti')


