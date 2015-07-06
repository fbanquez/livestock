# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api, _
#from odoo.exceptions import Warning

class livestock_corral(models.Model):
    _name = 'livestock.corral'
    _inherits = {'stock.warehouse': 'wharehouse_id'} 
    _description = "Livestock Corral model"
    _order = "wharehouse_id desc"

    def _purpose_corral_selection(self):
        return(('breeding', _("Breeding")),
               ('fattening', _("Fattening")),
               ('mating', _("Mating")),
               ('milking', _("Milking")),
               ('rest', _("Male Rest")))

    @api.one
    @api.depends('animal_ids')
    def _animals_amount_compute(self):
        self.animals = 0
        if self.id:
            query = """
            SELECT COUNT(id) 
            FROM livestock_animal 
            WHERE corral_id = %s 
            """
            self.env.cr.execute(query, (self.id,))
            reg = self.env.cr.fetchone()
            if reg[0]:
                self.animals = reg[0]

    def _topography_corral_selection(self):
        return(('flat', _("Flat")),
               ('soft_undulating', _("Soft Undulating")),
               ('undulating', _("Undulating")),
               ('broken', _("Broken")))

    def _water_corral_selection(self):
        return(('fountains', _("Fountains")),
               ('streams', _("Streams")),
               ('aqueducts', _("Aqueducts")),
               ('ditch', _("Ditch")),
               ('other', _("Other")))

    # Fields of the Corral Model
    wharehouse_id = fields.Many2one('stock.warehouse', string='Warehouse', required=True, ondelete='cascade', select=True, auto_join=True)
    purpose = fields.Selection(string='Purpose', selection=_purpose_corral_selection, required=True, help="Indicates the use that will give the corral")
    hectares = fields.Float(string='Hectares', digits=(7, 2), required=True, help="Number of acres comprising the corral")
    topography = fields.Selection(string='Topography', selection=_topography_corral_selection, required=True, help="Indicates the use that will give the corral")
    grass_prevalent = fields.Text(string='Grass Prevalent', required=False, help="Iindicates the kind of dominant grass on the corral")
    bush_prevalent = fields.Text(string='Bush Prevalent', required=False, help="Iindicates the kind of dominant bush on the corral")
    drinking_water = fields.Selection(string='Drinking Water', selection=_water_corral_selection, required=True, help="Source of water available in the corral")
    animals = fields.Integer(string='Animals', copy=False, compute='_animals_amount_compute', help="Numbers of animals into the corral")
    observation = fields.Text(string='Observation', required=False, help="Observations of corral")
    entry_date = fields.Date(string='Entry Date', default=None, help="Date since entering the first animal to the corral")
    rest_date = fields.Date(string='Rest Date', default=None, help="Date when the corral was empty")
    farm_id = fields.Many2one('livestock.farm', string='Farm', required=True, ondelete='cascade', index=True)
    animal_ids = fields.One2many('livestock.animal', 'corral_id', copy=False)
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable corral record")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
