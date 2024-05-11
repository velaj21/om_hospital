from odoo import fields, models, api


class Shift(models.Model):
    _name = 'hospital.shift'
    _description = 'Description'

    doctor_id = fields.Many2one(comodel_name='hospital.doctor', string='Doctor', required=True)
    TIME_SLOTS = [
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        # Add more time slots as needed
    ]

    start_time = fields.Selection(TIME_SLOTS, string='Start Time')
    end_time = fields.Selection(TIME_SLOTS, string='End Time')
