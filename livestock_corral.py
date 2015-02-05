# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api

class livestock_corral(models.Model):
    _name = 'livestock.corral'
    _inherit = 'stock.warehouse' 
    _description = "Livestock Corral model"
    _order = "key desc"

    def _purpose_corral_selection(self):
        return(('breeding', "Breeding"),
               ('fattening', "Fattening"),
               ('mating', "Mating"),
               ('fattening', "Fattening"),
               ('milking', "Milking"),
               ('rest', "Male Rest"))

    def _topography_corral_selection(self):
        return(('flat', "Flat"),
               ('soft_undulating', "Soft Undulating"),
               ('undulating', "Undulating"),
               ('broken', "Broken"))

    def _water_corral_selection(self):
        return(('fountains', "Fountains"),
               ('streams', "Streams"),
               ('aqueducts', "Aqueducts"),
               ('ditch', "Ditch"),
               ('other', "Other"))

    # Fields of the Corral Model
    key =  fields.Char(string='Identifier', size=8, required=True, help="Identifier of the corral")
    name = fields.Char(string='Name', size=25, required=True, select=True, help="Corral Name")
    purpose = fields.Selection(string='Purpose', selection=_purpose_corral_selection, required=True, help="Indicates the use that will give the corral")
    hectares = fields.Float(string='Hectares', digits=(7, 2), required=True, help="Number of acres comprising the corral")
    topography = fields.Selection(string='Topography', selection=_topography_corral_selection, required=True, help="Indicates the use that will give the corral")
    grass_prevalent = fields.Text(string='Grass Prevalent', required=False, help="Iindicates the kind of dominant grass on the corral")
    bush_prevalent = fields.Text(string='Bush Prevalent', required=False, help="Iindicates the kind of dominant bush on the corral")
    drinking_water = fields.Selection(string='Drinking Water', selection=_water_corral_selection, required=True, help="Source of water available in the corral")
    observation = fields.Text(string='Observation', required=False, help="Observations of corral")
    farm_id = fields.Many2one('livestock.farm', string='Farm', ondelete='cascade', index=True)
    #animal_ids = fields.One2many('livestock.animal', 'corral_id', copy=False)
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable corral record")

