from odoo import models, fields     
class plane_llibre(models.Model): 
    _name = 'plane.llibre' 
    codi = fields.Char('Codi', required=True) 
    titol = fields.Char('Títol', required=True)     
    isbn = fields.Char('ISBN', required=True)     
    pagines = fields.Char('Nombre de pàgines')   
    isbn = fields.Text('Descripció')