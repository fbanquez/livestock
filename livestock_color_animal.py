# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api

class livestock_color_animal(models.Model):
    _name = 'livestock.color.animal'
    _description = "Livestock Configuration Animal Color Model"
    _order = "race, color asc"

    def _race_color_selection(self):
        query = """
        SELECT features_type
        FROM livestock_race_category_animal
        WHERE name = 'race'
        AND active
        ORDER BY features_type
        """
        self.env.cr.execute(query)
        return [(row[0], row[0]) for row in self.env.cr.fetchall()]

    # Fields of the Configuration Animal Model
    race = fields.Selection(string='Race', required=True,  selection=_race_color_selection, index=True, help="Type of breed")
    color = fields.Char(string='Colour', index=True, required=True, help="Animal colour")
    description = fields.Text(string='Description', size=500, help="Long description of the animal characteristic")
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable features record")

