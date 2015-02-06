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

    @api.one
    @api.depends('measure_ids')
    def _measure_compute_date(self):
        id_key = self.id or 0
        query = """
        SELECT max(event_date)
          FROM livestock_thermo_event
         WHERE can_id = %s
           AND event_type = %s
       LIMIT 1
        """
        self.env.cr.execute(query, (id_key, 'measure'))
        reg = self.env.cr.fetchone()
        date_today = datetime.now().date()
        if reg[0] is None:
            date_measure = date_today
        else:
            date_measure = datetime.strptime(reg[0], '%Y-%m-%d').date()
        
        diff = date_today - date_measure
        self.last_measure = diff.days

    @api.one
    @api.depends('refill_ids')
    def _refill_compute_date(self):
        id_key = self.id or 0
        query = """
        SELECT max(event_date)
          FROM livestock_thermo_event
         WHERE can_id = %s
           AND event_type = %s
       LIMIT 1
        """
        self.env.cr.execute(query, (id_key, 'refill'))
        reg = self.env.cr.fetchone()
        date_today = datetime.now().date()
        if reg[0] is None:
            date_measure = date_today
        else:
            date_measure = datetime.strptime(reg[0], '%Y-%m-%d').date()
        
        diff = date_today - date_measure
        self.last_refill = diff.days

    # Fields of the Thermo Model
    name = fields.Char(string='Identifier', size=8, required=True, select=True, help="Thermo Identifier")
    characteristics =  fields.Char(string='Characteristics', size=50, required=True, help="Thermo characeristics")
    capacity = fields.Float(string='Capacity', digits=(5, 2), required=True, help="Thermo Capacity in liters")
    racks = fields.Integer(string='Racks', required=True, help="Numbers of racks into the thermo")
    shelves = fields.Integer(string='Shelves', required=True, help="Numbers of shelves into the rack's thermo")
    created_date = fields.Date(string='Created', default=datetime.now(), required=True, help="Effective date of the thermo first use")
    purpose = fields.Selection(string='Purpose', selection=_purpose_thermo_selection, required=True, help="Thermo purpose. Store embryos or semen")
    straws_ids = fields.One2many('livestock.straw', 'thermo_id', string=None, copy=False)
    last_measure = fields.Integer(string='Last Measure', copy=False, readonly=True, compute='_measure_compute_date', help="Days since the last measurement of nitrogen")
    last_refill = fields.Integer(string='Last Refill', copy=False, readonly=True, compute='_refill_compute_date', help="Days since last refill of nitrogen")
    measure_ids = fields.One2many('livestock.thermo.event', 'can_id', copy=False, domain=[('event_type','=','measure')])
    refill_ids = fields.One2many('livestock.thermo.event', 'can_id', copy=False, domain=[('event_type','=','refill')])
    farm_id = fields.Many2one('livestock.farm', string='Farm', ondelete='cascade')
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

