from odoo import models, fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    codi = fields.Integer('Codi')
    nom = fields.Char('Nom', required=True)
    imatge = fields.Char('https://www.google.com/search?q=imatge&rlz=1C1UEAD_esES1053ES1053&source=lnms&tbm=isch&sa=X&ved=2ahUKEwip1uDIvon_AhUi7LsIHVDcBjMQ_AUoAXoECAEQAw&biw=1512&bih=826#imgrc=AVwaL8Crxq4cdM')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')
    latitud = fields.Float('Latitud')
    longitud = fields.Float('Longitud')
    volOrigen_id = fields.One2many('plane.vol','aeroportOrgien_id',string = 'Orgien')
    volDesti_id = fields.One2many('plane.vol','aeroportDesti_id',string = 'Desti')
    



    