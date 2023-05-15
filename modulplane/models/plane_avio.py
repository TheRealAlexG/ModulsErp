from odoo import models, fields     
class plane_avio(models.Model): 
    _name = 'plane.avio' 
    codi = fields.Integer('Codi', required=True) 
    imatge = fields.Char('https://www.google.com/search?q=plane&rlz=1C5CHFA_enES993ES993&sxsrf=APwXEdcpsvjqNyC8X1GwAZw-Xzj-PV5pmQ:1683569665334&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi9g-3eqeb-AhW6VqQEHdDSDT4Q_AUoAXoECAIQAw&biw=1512&bih=871&dpr=2#imgrc=jLI-gPnuY_4pIM', required=True)     
    marca = fields.Integer('Marca')
    model = fields.Char('Model')
    maxVal = fields.Float('MaxVel')
    
