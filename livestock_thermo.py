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
    capacity = fields.Float(string='Capacity', digits=(5, 2), required=True, help="Thermo Capacity in liters")
    racks = fields.Integer(string='Racks', required=True, help="Numbers of racks into the thermo")
    shelves = fields.Integer(string='Shelves', required=True, help="Numbers of shelves into the rack's thermo")
    created_date = fields.Date(string='Created', default=datetime.now(), required=True, help="Effective date of the thermo first use")
    purpose = fields.Selection(string='Purpose', selection=_purpose_thermo_selection, required=True, help="Thermo purpose. Store embryos or semen")
    farm = fields.Char(string='Farm', size=25, required=True, help="Farm where thermo was created")
    straws_ids = fields.One2many('livestock.straw', 'thermo_id', string=None, copy=False)
    measure_ids = fields.One2many('livestock.thermo.event', 'can_id', copy=False, domain=[('event_type','=','measure')])
    refill_ids = fields.One2many('livestock.thermo.event', 'can_id', copy=False, domain=[('event_type','=','refill')])
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable thermo record")


class livestock_thermo_event(models.Model):
    _name = 'livestock.thermo.event'
    _description = "Livestock Thermo event for nitrogen measurement or reloading"
    _order = "event_date desc"

    # Fields of the Nitrogen_Thermo Model
    name = fields.Char(string='Responsible', size=25, required=True, select=True, default=lambda self: self.env.user.name, help="Straw name")
    event_date = fields.Date(string='Date', default=datetime.now(), required=True, help="Event date")
    nitrogen_amount = fields.Float(string='Amount', digits=(5, 2), required=True)
    event_type = fields.Selection(string='Event', selection=[('measure', 'Measurement'), ('refill', 'Refill')], required=True)
    can_id = fields.Many2one('livestock.thermo', string='Thermo', ondelete='cascade', index=True)

