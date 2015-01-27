# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api

class livestock_thermo(models.Model):
    _name = 'livestock.thermo'
    _description = "Livestock Thermo model"
    _order = "name desc"

    def _purpose_thermo_selection(self):
        return(('embryo', "Embryo"),
               ('semen', "Semen"))

    # Fields of the Thermo Model
    name = fields.Char(string='Identifier', size=8, required=True, select=True, help="Thermo Identifier")
    characteristics =  fields.Char(string='Characteristics', size=50, required=True, help="Thermo characeristics")
    capacity = fields.Float(string='Capacity', required=True, help="Thermo Capacity in liters")
    racks = fields.Integer(string='Racks', required=True, help="Numbers of racks into the thermo")
    shelves = fields.Integer(string='Shelves', required=True, help="Numbers of shelves into the rack's thermo")
    created_date = fields.Date(string='Created', default=datetime.now(), required=True, help="Effective date of the thermo first use")
    purpose = fields.Selection(string='Purpose', selection=_purpose_thermo_selection, required=True, help="Thermo purpose. Store embryos or semen")
    farm = fields.Char(string='Farm', size=25, required=True, help="Farm where thermo was created")
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable record")

