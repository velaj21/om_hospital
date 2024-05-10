# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Doctor"
    _rec_name = 'doctor_name'

    # todo beje nje tabel te re per ratings qe i jep doktorrit dhe gjej mesataren e tij
    average_rating = fields.Float(string='Average Rating', compute='_compute_average_rating', store=True)

    # todo vendos email dhe nr telefoni bej valid vtm per shqiperin
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
    # rating_ids = fields.One2many('hospital.rating', 'doctor_id', string='Ratings')
    appointment_ids = fields.Many2one('hospital.appointment', string='Ratings')

    def compute_avg_rate(self):
        pass

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

    # def _compute_average_rating(self):
    #     for rec in self:
    #         total_rating = sum(rec.rating_ids.mapped('rating'))
    #         if rec.rating_ids:
    #             rec.average_rating = total_rating / len(rec.rating_ids)
    #         else:
    #             rec.average_rating = 0.0

    def _compute_average_rating(self):
        for doctor in self:
            total_rating = 0.0
            num_ratings = 0
            for appointment in doctor.appointment_ids:
                if appointment.rating:
                    total_rating += appointment.rating
                    num_ratings += 1
            if num_ratings:
                doctor.average_rating = total_rating / num_ratings
            else:
                doctor.average_rating = 0.0

# todo krijo nje model te ri turni vendose me 3 psh
# todo krijo 1 tabel tjt orari i turnit
# todo krjo nje tabel turni_i_doktorrit qe ka daten me turnin e tij
# todo do ndryshohet tani llogjika e appointment qe do zgjedhesh turnin
# bashke me oren dhe do behet dicka per filtrimin qe te maresh keta doktora per turn
