from odoo import models, fields
class zoo_zoo(models.Model):
    _name = 'zoo.zoo'
    nom = fields.Char('Nom', required=True)
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')
    grandaria = fields.Float('Grandaria')
    id = fields.Integer('ID')