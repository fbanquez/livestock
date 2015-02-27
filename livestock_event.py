# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api

class livestock_event(models.Model):
    _name = 'livestock.event'
    _description = "Livestock Event Model"
    _order = "created_date desc"

    def _event_type_event_selection(self):
        return(('gestation', "Gestation"),
               ('palpation', "Palpation"),
               ('other', "Other"))

    # Fields of the Event Model
    name = fields.Char(string='Name', size=20, required=True, help="Name of the event")
    event_type = fields.Selection(string='Type', selection=_event_type_event_selection, required=True, help="Event type")
    description = fields.Text(string='Description', required=True, help="Long description of the event")
    created_date = fields.Datetime(string='Date', required=True, default=datetime.now(), help="Date on which the event occurred")
    responsible = fields.Char(string='Responsible', required=True, size=30, default=lambda self: self.env.user.name, help="Person who reported the event")
    animal_id = fields.Many2one('livestock.animal', string='Animal', ondelete='cascade', index=True)
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable event record")

