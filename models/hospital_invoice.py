from odoo import fields, models, api


class HospitalInvoice(models.Model):
    _name = 'hospital.invoice'

    number = fields.Char(string='Number')
    patient_id = fields.Many2one(comodel_name='hospital.doctor', string='Patient_id')
    # doctor_id = fields.Many2one(comodel_name='hospital.doctor', string='Patient_id')

