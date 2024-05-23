from xlrd.xlsx import ET
import re

from odoo import models, fields, api
import base64


class MyWizard(models.TransientModel):
    _name = 'my.wizard'
    _description = 'My Wizard'

    file = fields.Binary(string='Vendosni file ne format xml', required=True)
    is_valid = fields.Boolean(string='Field 2', default=False, readonly=True)

    def validate_xml(self):
        file_content = base64.b64decode(self.file).decode('utf-8')

        root = ET.fromString(file_content)

        # Find SendDateTime attribute
        send_datetime = root.find('.//{http://example.com/ns3}Header').attrib.get('SendDateTime')

        # Check if SendDateTime exists and has correct format
        if send_datetime and len(send_datetime) == 36 and re.match(
                r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$',
                send_datetime):
            # Set is_valid field to True if validation succeeds
            self.is_valid = True
        else:
            # Set is_valid field to False if validation fails
            self.is_valid = False

        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
