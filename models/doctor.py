# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import re


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Doctor"
    _rec_name = 'doctor_name'

    _sql_constraints = [
        ('unique_email', 'UNIQUE(email)', 'The email must be unique.'),
        ('unique_phone', 'UNIQUE(phone)', 'The phone number must be unique.')
    ]

    email = fields.Char(string='Email', required=True, tracking=True)
    doctor_name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True, copy=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    note = fields.Text(string='Description')
    image = fields.Binary(string="Patient Image")
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
    active = fields.Boolean(string="Active", default=True)
    rating_ids = fields.One2many('hospital.rating', 'doctor_id', string='Ratings')
    appointment_ids = fields.One2many(comodel_name='hospital.appointment', inverse_name='doctor_id',
                                      string='Appointments')
    average_rating = fields.Float(string='Average Rating', compute='_compute_average_rating', store=True)
    phone = fields.Char(string='Phone', required=True, tracking=True)
    # shift_ids = fields.One2many('hospital.shift', 'doctor_id', string='Shifts')
    shift_id = fields.Many2one(comodel_name='hospital.shift', string='Shift id')
    current_shift_type = fields.Char(string='Current Shift Type', compute='_compute_current_shift_type', store=True)

    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('doctor_name'):
            default['doctor_name'] = _("%s (Copy)", self.doctor_name)
        default['note'] = "Copied Record"
        return super(HospitalDoctor, self).copy(default)

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['hospital.appointment'].search_count([('doctor_id', '=', rec.id)])
            rec.appointment_count = appointment_count

    @api.depends('rating_ids.rating')
    def _compute_average_rating(self):
        for doctor in self:
            ratings = doctor.rating_ids.mapped('rating')
            if ratings:
                doctor.average_rating = sum(int(rating) for rating in ratings) / len(ratings)
            else:
                doctor.average_rating = 0.0

    @api.constrains('email')
    def _check_email_format(self):
        for record in self:
            if record.email:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", record.email):
                    raise ValidationError(_("Invalid email format. Please provide a valid email address."))

    @api.constrains('phone')
    def _check_phone_format(self):
        for record in self:
            if record.phone:
                if not re.match(r"\+355[0-9]{9}$", record.phone):
                    raise ValidationError(
                        _("Invalid phone number format."
                          " Albanian phone numbers should start with '+355' followed by 9 digits."))

    @api.depends('shift_id')
    def _compute_current_shift_type(self):
        for doctor in self:
            if doctor.shift_id:
                doctor.current_shift_type = doctor.shift_id.shift_type
            else:
                doctor.current_shift_type = False

# todo krijo nje model te ri turni vendose me 3 psh
# todo krijo 1 tabel tjt orari i turnit
# todo krjo nje tabel turni_i_doktorrit qe ka daten me turnin e tij
# todo do ndryshohet tani llogjika e appointment qe do zgjedhesh turnin
# bashke me oren dhe do behet dicka per filtrimin qe te maresh keta doktora per turn
