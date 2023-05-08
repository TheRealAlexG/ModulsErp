from odoo import models, fields     
class zoo_animal(models.Model): 
    _name = 'zoo.animal' 
    id = fields.Integer('ID')
    continentOrigen = fields.Char('Continent Origen', required=True) 
    dataNaix = fields.Date('Data Naixament')     
    paisOrigen = fields.Char('Pais Origen')     
    sexe = fields.Char('Sexe')