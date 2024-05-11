from odoo import fields, models, api


class Shift(models.Model):
    _name = 'hospital.shift'
    _description = 'Description'

    doctor_id = fields.Many2one(comodel_name='hospital.doctor', string='Doctor', required=True)
    TIME_SLOTS = [
        ('08:00', '05:00'),
        ('05:00', '12:00'),
        ('12:00', '8:00'),
    ]

    start_time = fields.Selection(TIME_SLOTS, string='Start Time')
    end_time = fields.Selection(TIME_SLOTS, string='End Time')
