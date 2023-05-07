from odoo import models, fields     
class plane_editorial(models.Model): 
    _name = 'plane.editorial' 
    nom = fields.Char('Nom', required=True) 
    adreca = fields.Char('Adreça')     
    telf = fields.Char('Telèfon')     
    email = fields.Char('Correu electrònic')