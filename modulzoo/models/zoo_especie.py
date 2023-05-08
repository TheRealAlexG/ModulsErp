from odoo import models, fields     
class zoo_especie(models.Model): 
    _name = 'zoo.especie' 
    id = fields.Integer('ID')
    familia = fields.Char('Familia')     
    nomCientific = fields.Char('Nom Cientific')     
    nomVulgar = fields.Char('Nom Vulgar')
    perill = fields.Char('Perill')

    