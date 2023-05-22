from odoo import models, fields     
class plane_avio(models.Model): 
    _name = 'plane.avio' 
    codi = fields.Integer('Codi', required=True) 
    imatge = fields.Char('https://www.google.com/search?q=imatge&rlz=1C1UEAD_esES1053ES1053&source=lnms&tbm=isch&sa=X&ved=2ahUKEwip1uDIvon_AhUi7LsIHVDcBjMQ_AUoAXoECAEQAw&biw=1512&bih=826#imgrc=AVwaL8Crxq4cdM', required=True)     
    marca = fields.Integer('Marca')
    model = fields.Char('Model')
    maxVal = fields.Float('MaxVel')
    vol_ids = fields.One2many('plane.vol','avio_id',string ='vol')
    
