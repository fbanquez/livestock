# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api, _

class livestock_color_animal(models.Model):
    _name = 'livestock.color.animal'
    _description = "Configuration Model Animal Color in Livestock"
    _order = "name"

    # Fields of the Configuration Animal Model
    name = fields.Char(string='Color', index=True, required=True, help="Animal color")
    description = fields.Text(string='Description', size=500, help="Long description of the animal color")
    animal_id = fields.One2many('livestock.animal', 'colour_id', copy=False)
    race_id = fields.Many2one(comodel_name='livestock.race.animal', string='Race', ondelete='set null', index=True)
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable color record")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
