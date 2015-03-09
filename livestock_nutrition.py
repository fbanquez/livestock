# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api, _

class livestock_nutrition(models.Model):
    _name = 'livestock.nutrition'
    _description = "Livestock Nutrition Model"
    _order = "name desc"

    def _administration_route_nutrition_selection(self):
        return(('orally', _("Orally")),
               ('sublingual', _("Sublingual")),
               ('intramuscular', _("Intramuscular")),
               ('intravenous', _("Intravenous")),
               ('cutaneous', _("Cutaneous")),
               ('subcutaneous', _("Subcutaneous")),
               ('rectal', _("Rectal")))

    def _supporting_feature_nutrition_selection(self):
        return(('provender', _("Provender")),
               ('supplement', _("Supplement")))

    # Fields of the Event Model
    name = fields.Selection(string='Supporting Feature', required=True, selection=_supporting_feature_nutrition_selection, help="Nutritional supplement to be dispensed")
    supplement_type = fields.Char(string='SF Type', size=25, required=True, help="Nutritional supplement type to be dispensed")
    manufacturing_lab = fields.Char(string='Laboratory/Factory', size=20, required=True, help="Household manufactured the nutritional supplement")
    batch_manufacture = fields.Char(string='Lot', size=20, required=True, help="Batch manufacture of nutritional products")
    dosage = fields.Text(string='Dosage', required=True, help="Dose to be dispensed to the animal")
    administration_route = fields.Selection(string='Administration Routes', selection=_administration_route_nutrition_selection, required=True, help="Routes of administration of nutritional supplement")
    application_frequency = fields.Char(string='Application Frequency', size=25, required=True, help="Frequency at which the nutritional supplement should be dispensed")
    responsible = fields.Char(string='Responsible', required=True, size=30, default=lambda self: self.env.user.name, help="Person administering the supplement")
    animal_id = fields.Many2one('livestock.animal', string='Animal', ondelete='cascade', index=True)
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable nutrition record")

