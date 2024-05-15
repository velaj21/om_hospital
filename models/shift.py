from odoo import fields, models, api


class Shift(models.Model):
    _name = 'hospital.shift'
    _description = 'Description'

    doctor_id = fields.Many2one(comodel_name='hospital.doctor', string='Doctor', required=True)

    TIME_SLOTS_AM_PM = [
        ('00:00', '12:00 AM'),
        ('01:00', '01:00 AM'),
        ('02:00', '02:00 AM'),
        ('03:00', '03:00 AM'),
        ('04:00', '04:00 AM'),
        ('05:00', '05:00 AM'),
        ('06:00', '06:00 AM'),
        ('07:00', '07:00 AM'),
        ('08:00', '08:00 AM'),
        ('09:00', '09:00 AM'),
        ('10:00', '10:00 AM'),
        ('11:00', '11:00 AM'),
        ('12:00', '12:00 PM'),
        ('13:00', '01:00 PM'),
        ('14:00', '02:00 PM'),
        ('15:00', '03:00 PM'),
        ('16:00', '04:00 PM'),
        ('17:00', '05:00 PM'),
        ('18:00', '06:00 PM'),
        ('19:00', '07:00 PM'),
        ('20:00', '08:00 PM'),
        ('21:00', '09:00 PM'),
        ('22:00', '10:00 PM'),
        ('23:00', '11:00 PM'),
    ]

    start_date = fields.Date(string='Start date', required=True)
    end_date = fields.Date(string='End date', required=True)
    shift_type = fields.Selection(
        string='Shift_type',
        selection=[('Morning', 'Morning'),
                   ('Evening', 'Evening'),
                   ('Night', 'Night')],
        required=True)

    start_time = fields.Selection(TIME_SLOTS_AM_PM, string='Start Time', required=True)
    end_time = fields.Selection(TIME_SLOTS_AM_PM, string='End Time', required=True)
