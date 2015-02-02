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
    name = fields.Char(string='Identifier', size=8, required=True, select=True, help="Alphanumeric identifier embryo")
    species =  fields.Char(string='Species', size=20, required=True, help="Animal species")
    race = fields.Char(string='Race', size=45, required=True, help="Animal race")
    mother = fields.Char(string='Mother', size=25, required=True, help="Female donor")
    father = fields.Char(string='Father', size=25, required=True, help="Male donor")
    phase = fields.Selection(string='Phase', selection=_phase_embryo_selection, required=True, help="Phase embryo")
    quality = fields.Selection(string='Quality', selection=_quality_embryo_selection, required=True, help="Quality embryo")
    created_date = fields.Date(string='Created', default=datetime.now(), required=True, help="Date of creation of the embryo")
    farm = fields.Char(string='Farm', size=25, required=True, help="Farm where the embryo was created")
    responsible = fields.Char(string='Responsible', size=25, required=True, default=lambda self: self.env.user.name, help="Biologist, veterinarian or person responsible for the creation of the embryo")
    straw_id = fields.Many2one('livestock.straw', string='Straw', ondelete='cascade', index=True)
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable record")

