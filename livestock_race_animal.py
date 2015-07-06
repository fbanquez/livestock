# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api, _

class livestock_race_animal(models.Model):
    _name = 'livestock.race.animal'
    _description = "Configuration Model Animal Race in Livestock"
    _order = "name"

    # Fields of the Configuration Animal Model
    name = fields.Char(string='Race', index=True, required=True, help="Animal race")
    description = fields.Text(string='Description', size=500, help="Long description of the animal race")
    animal_id = fields.One2many('livestock.animal', 'race_id', copy=False)
    specie_id = fields.Many2one(comodel_name='livestock.specie.animal', string='Specie', ondelete='set null', index=True)
    color_ids = fields.One2many('livestock.color.animal', 'race_id', copy=False)
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable race record")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
