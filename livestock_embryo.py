# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api

class livestock_embryo(models.Model):
    _name = 'livestock.embryo'
    _description = "Livestock Embryo model"
    _order = "id desc"

    def _phase_embryo_selection(self):
        return(('m', "Morula"),
               ('mc', "Morula Compacta"),
               ('bt', "Blastocisto Temprano"),
               ('bx', "Blastocisto Expandido"),
               ('bc', "Blastocisto Eclosionado"))

    def _quality_embryo_selection(self):
        return(('c1', "Calidad 1"),
               ('c2', "Calidad 2"),
               ('c3', "Calidad 3"),
               ('c4', "Calidad 4"))

    # Fields of the Embryo Model
    name = fields.Char(string='Identifier', size=8, required=True, select=True)
    species =  fields.Char(string='Species', size=20, required=True)
    race = fields.Char(string='Race', size=45, required=True)
    mother = fields.Char(string='Mother', size=25, required=True)
    father = fields.Char(string='Father', size=25, required=True)
    phase = fields.Selection(string='Phase', selection=_phase_embryo_selection, required=True)
    quality = fields.Selection(string='Quality', selection=_quality_embryo_selection, required=True)
    created_date = fields.Date(string='Created', default=datetime.now().strftime('%Y-%m-%d'), required=True)
    farm = fields.Char(string='Farm', size=25, required=True)
    responsible = fields.Char(string='Responsible', size=25, required=True)
    location = fields.Char(string='Straw', size=25, required=True)
    active = fields.Boolean(string='Active', default=True)

