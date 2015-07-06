# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api, _

class livestock_specie_animal(models.Model):
    _name = 'livestock.specie.animal'
    _description = "Configuration Model Animal Specie in Livestock"
    _order = "name"

    # Fields of the Configuration Animal Model
    name = fields.Char(string='Specie', index=True, required=True, help="Animal specie")
    description = fields.Text(string='Description', size=500, help="Long description of the animal specie")
    #animal_id = fields.Many2one(comodel_name='livestock.animal', string='Animal', ondelete='cascade', index=True)
    animal_id = fields.One2many('livestock.animal', 'specie_id', copy=False)
    race_ids = fields.One2many('livestock.race.animal', 'specie_id', string='Race', copy=False, help="Animal Race")
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable specie record")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
