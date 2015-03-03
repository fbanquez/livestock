# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api

class livestock_animal(models.Model):
    _name = 'livestock.animal'
    _inherits = {'product.product': 'prod_id'} 
    _description = "Livestock Animal model"
    _order = "id, born_date desc"

    def _species_animal_selection(self):
        return(('milk', "Milk"),
               ('dual', "Dual Purpose"),
               ('commercial', "Commercial Breeding"),
               ('fattening', "Fattening"))

    def _race_animal_selection(self):
        return(('milk', "Milk"),
               ('dual', "Dual Purpose"),
               ('commercial', "Commercial Breeding"),
               ('fattening', "Fattening"))

    def _gestation_animal_selection(self):
        return(('mating', "Natural Mating"),
               ('biotechnology', "Biotechnology"))

    def _biotech_animal_selection(self):
        return(('insemination', "Artificial Insemination"),
               ('washing', "Sperm Washing"),
               ('aspiration', "Follicular Aspiration"))

    @api.one
    def _get_image(self):
        return dict((s.id, tools.image_get_resized_images(s.image)) for s in self)

    @api.one
    def _set_image(self):
        return self.write({'image': tools.image_resize_image_big(value)})
        
    # Fields of the Animal Model
    prod_id = fields.Many2one('product.product', string='Parent', required=True, ondelete='cascade', select=True, auto_join=True)
    species = fields.Selection(string='Species', selection=_species_animal_selection, required=True, help="Animal species")
    race = fields.Selection(string='Race', selection=_race_animal_selection, required=True, help="Breed of animal")
    category = fields.Char(string='Category', size=45, required=True, help="Animal category")
    gestation = fields.Selection(string='Gestation', selection=_gestation_animal_selection, required=True, help="Type of gestation")
    biotech = fields.Selection(string='Biotechnology', selection=_biotech_animal_selection, required=False, help="Type of biotechnology that suitable gestation")
    registration = fields.Char(string='Registration', size=8, required=True, help="Identification of an animal to an association of farmers")
    gender = fields.Selection(string='Gender', selection=[('female', 'Female'), ('male', 'Male')], required=True, help="Animal gender")
    repro_stage = fields.Char(string='Reproductive Stage', size=50, required=True, help="Reproductive stage of the animal") #compute=
    birth_weight = fields.Float(string='Birth Weight', digits=(4, 2), required=True, help="Animal birth weight")
    born_date = fields.Date(string='Born Date', default=datetime.now(), required=True, help="Date of birth of the animal")
    labour_type = fields.Char(string='Labour Type', size=30, required=True, help="Type of birth of the animal")
    corral_id = fields.Many2one('livestock.corral', string='Corral', ondelete='set null', index=True)
    female_parent_id = fields.Many2one('livestock.animal', string='Mother', ondelete='set null', index=True)
    male_parent_id = fields.Many2one('livestock.animal', string='Father', ondelete='set null', index=True)
    disease_ids = fields.One2many('livestock.disease', 'animal_id', string=None, copy=False)
    nutrition_ids = fields.One2many('livestock.nutrition', 'animal_id', string=None, copy=False)
    weighing_ids = fields.One2many('livestock.weighing', 'animal_id', string=None, copy=False)
    event_ids = fields.One2many('livestock.event', 'animal_id', string=None, copy=False)

    #@api.model
    #def create(self, values):
    #    print values
    #    ctx = self.env.context
    #    print ctx
    #    return reg = super(livestock_animal, self).create(values)

