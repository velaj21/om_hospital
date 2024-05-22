# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import re
import requests


class Word(models.Model):
    _name = "word.word"
    _description = "Word"

    name = fields.Char(string='WORD')

    def generate_words(self):
        url1 = 'https://random-word-api.herokuapp.com/word?number=10'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

        r = requests.get(url1, headers=headers)  # Dergon http get request
        r.raise_for_status()  # ben throw error nqs statusi eshte i ndryshem nga 200
        data = r.json()  # formaton response ne json

        for rec in data:
            if rec:
                self.create({'name': rec})
