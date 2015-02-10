# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api

class livestock_weighing(models.Model):
    _name = 'livestock.weighing'
    _description = "Livestock Weighing Model"
    _order = "created_date desc"

    # Fields of the Weighing Model
    name = fields.Char(string='Identifier', size=8, required=True, help="Identifier of the Weighing")
    current_weight = fields.Integer(string='Current Weight', required=True, help="Current animal weight")
    created_date = fields.Datetime(string='Date', required=True, default=datetime.now(), help="Date on which the event occurred")
    daily_gain = fields.Float(string='Daily Gain', digits=(6, 2), required=True, help="Daily weight gain of the animal")
    life_gain = fields.Float(string='Life Gain', digits=(6, 2), required=True, help="Grams profit animal life")
    projecting_days = fields.Integer(string='Projecting Days', required=True, help="Projected number of days")
    adjusted_weight = fields.Float(string='Adjusted Weight', digits=(6, 2), required=True, help="Animal weight set")
    responsible = fields.Char(string='Responsible', required=True, size=30, default=lambda self: self.env.user.name, help="Person who made the weigh")
    comment = fields.Text(string='Comment', required=False, help="Comments about weighing the animal")
    #animal_id = fields.Many2one('livestock.animal', string='Animal', ondelete='cascade', index=True)
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable weighing record")

