# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api, _

class livestock_race_category_animal(models.Model):
    _name = 'livestock.race.category.animal'
    _description = "Livestock Configuration Race, Category and Species Animal Model"
    _order = "name, features_type asc"

    def _features_conf_animal_selection(self):
        return(('species', _("Species")),
               ('race', _("Race")),
               ('category', _("Category")))

    # Fields of the Configuration Animal Model
    name = fields.Selection(string='Features', index=True, selection=_features_conf_animal_selection, required=True, help="Animal characteristic")
    features_type = fields.Char(string='Feature Type', size=25, required=True, help="Features type")
    description = fields.Text(string='Description', size=500, help="Long description of the animal characteristic")
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable features record")

