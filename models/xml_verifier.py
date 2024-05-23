import os.path
import xml.etree.ElementTree as ET
from odoo import fields, models, api


class XmlVerifier(models.Model):
    _name = 'xml.verifier'
