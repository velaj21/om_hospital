from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Shift(models.Model):
    _name = 'hospital.shift'
    _description = 'Description'

    doctor_ids = fields.One2many(comodel_name='hospital.doctor', inverse_name='shift_id', string='Doctor ids')

    doctor_names = fields.Char(string='Doctor Names', compute='_compute_doctor_names', store=True)

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
        String='Shift Type', compute='_compute_shift_type')

    start_time = fields.Selection(TIME_SLOTS_AM_PM, string='Start Time', required=True)
    end_time = fields.Selection(TIME_SLOTS_AM_PM, string='End Time', required=True)

    # @api.depends('doctor_ids')
    # def _compute_readonly_doctor_ids(self):
    #     for shift in self:
    #         shift.readonly_doctor_ids = bool(shift.doctor_ids)
    #
    # readonly_doctor_ids = fields.Boolean(compute='_compute_readonly_doctor_ids', store=True)

    @api.depends('doctor_ids')
    def _compute_doctor_names(self):
        for shift in self:
            shift.doctor_names = ', '.join(doctor.doctor_name for doctor in shift.doctor_ids)

    @api.depends('start_time')
    def _compute_shift_type(self):
        for shift in self:
            if shift.start_time:
                start_hour = int(shift.start_time.split(':')[0])
                if 6 <= start_hour < 12:
                    shift.shift_type = 'Morning'
                elif 12 <= start_hour < 18:
                    shift.shift_type = 'Evening'
                else:
                    shift.shift_type = 'Night'
                break
            else:
                shift.shift_type = False

    @api.constrains('start_date', 'end_date', 'start_time', 'end_time')
    def _check_conflicting_shifts(self):
        for shift in self:
            domain = [
                ('id', '!=', shift.id),
                ('start_date', '<=', shift.end_date),
                ('end_date', '>=', shift.start_date),
                ('start_time', '<', shift.end_time),
                ('end_time', '>', shift.start_time),
            ]
            conflicting_shifts = self.search(domain)
            if conflicting_shifts:
                raise ValidationError('Conflicting shifts found!')
