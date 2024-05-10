# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Doctor"
    _rec_name = 'doctor_name'

    # todo beje nje tabel te re per ratings qe i jep doktorrit dhe gjej mesataren e tij
    rateDoctorin = fields.Integer(
        string='RateDoctorin',
        required=False)
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


# todo krijo nje model te ri turni vendose me 3 psh
# todo krijo 1 tabel tjt orari i turnit
# todo krjo nje tabel turni_i_doktorrit qe ka daten me turnin e tij
