from odoo import models, fields, api
import base64

class MyWizard(models.TransientModel):
    _name = 'my.wizard'
    _description = 'My Wizard'

    file = fields.Binary(string='Vendosni file ne format xml', required=True)
    is_valid = fields.Boolean(string='Field 2', default=False, readonly=True)

    def validate_xml(self):
        file_content = base64.b64decode(self.file).decode('utf-8')
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
