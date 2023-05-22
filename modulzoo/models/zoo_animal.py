from odoo import models, fields     
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    continentOrigen = fields.Char('Continent Origen', required=True)
    dataNaix = fields.Date('Data Naixament')
    paisOrigen = fields.Char('Pais Origen')    
    sexe = fields.Char('Sexe')
    zoo_id = fields.Many2one('zoo.zoo', string ='zoo')
    especie_id = fields.Many2one('zoo.especie', string ='especie')