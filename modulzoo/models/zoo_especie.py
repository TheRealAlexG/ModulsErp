from odoo import models, fields     
class zoo_editorial(models.Model): 
    _name = 'zoo.editorial' 
    nom = fields.Char('Nom', required=True) 
    adreca = fields.Char('Adreça')     
    telf = fields.Char('Telèfon')     
    email = fields.Char('Correu electrònic')

    