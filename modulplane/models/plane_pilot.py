from odoo import models, fields     
class plane_pilot(models.Model): 
    _name = 'plane.pilot' 
    codi = fields.Integer('Codi', required=True) 
    nom = fields.Char('Nom', required=True)
    Cognoms = fields.Char('Cognoms', required=True)     
    nif = fields.Char('NIF', required=True)     
    telf = fields.Char('Telf')   
    email = fields.Text('Email')
    vols_id = fields.One2many('plane.vol','pilot_id',string = 'vols')
    