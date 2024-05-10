from odoo import fields, models, api


class Rating(models.Model):
    _name = 'hospital.rating'

    doctor_id = fields.Many2one(comodel_name='hospital.doctor', string='Doctor_id')
    rating = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Rating', required=True)
    comment = fields.Text(string='Comment')
