from odoo import fields, models, api


class Rating(models.Model):
    _name = 'hospital.rating'

    doctor_id = fields.Many2one(comodel_name='hospital.doctor', string='Doctor_id')
    rating = fields.Float(string='Rating', required=True)
    comment = fields.Text(string='Comment')
