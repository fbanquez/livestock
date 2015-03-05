# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api

class livestock_animal(models.Model):
    _name = 'livestock.animal'
    _inherits = {'product.product': 'prod_id'} 
    _description = "Livestock Animal model"
    _order = "id, born_date desc"

    def _species_animal_selection(self):
        query = """
        SELECT features_type
        FROM livestock_race_category_animal
        WHERE name = 'species'
        AND active
        ORDER BY features_type
        """
        self.env.cr.execute(query)
        return [(row[0], row[0]) for row in self.env.cr.fetchall()]

    def _race_animal_selection(self):
        query = """
        SELECT features_type
        FROM livestock_race_category_animal
        WHERE name = 'race'
        AND active
        ORDER BY features_type
        """
        self.env.cr.execute(query)
        return [(row[0], row[0]) for row in self.env.cr.fetchall()]

    @api.depends('race')
    def _colour_animal_selection(self):
        if self.race:
            query = """SELECT color FROM livestock_color_animal WHERE race = %s
            AND active ORDER BY color"""
            self.env.cr.execute(query, (self.race))
        else:
            query = """SELECT distinct(color) FROM livestock_color_animal WHERE active
            ORDER BY color"""
            self.env.cr.execute(query)
        return [(row[0], row[0]) for row in self.env.cr.fetchall()]

    def _condition_animal_selection(self):
        return [(str(n), str(n)) for n in range(1, 10)]

    @api.one
    @api.depends('born_date')
    def _age_animal_compute(self):
        self.age = 0
        if self.born_date:
            today = datetime.now().date()
            bday = datetime.strptime(self.born_date, '%Y-%m-%d').date()
            self.age = (today.year - bday.year)*12 + today.month - bday.month + (-1 if bday.day > today.day else 0)

    def _category_animal_selection(self):
        query = """
        SELECT features_type
        FROM livestock_race_category_animal
        WHERE name = 'category'
        AND active
        ORDER BY features_type
        """
        self.env.cr.execute(query)
        return [(row[0], row[0]) for row in self.env.cr.fetchall()]

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
    age = fields.Integer(string='Age', copy=False, readonly=True, compute='_age_animal_compute', help="Age of the animal in months")
    species = fields.Selection(string='Species', selection=_species_animal_selection, required=True, help="Animal species")
    race = fields.Selection(string='Race', selection=_race_animal_selection, required=True, help="Breed of animal")
    colour = fields.Selection(string='Colour', selection=_colour_animal_selection, required=True, help="Color of animal")
    category = fields.Selection(string='Category',  selection=_category_animal_selection, required=True, help="Animal category")
    gestation = fields.Selection(string='Gestation', selection=_gestation_animal_selection, required=True, help="Type of gestation")
    biotech = fields.Selection(string='Biotechnology', selection=_biotech_animal_selection, required=False, help="Type of biotechnology that suitable gestation")
    registration = fields.Char(string='Registration', size=8, required=True, help="Identification of an animal to an association of farmers")
    gender = fields.Selection(string='Gender', selection=[('female', 'Female'), ('male', 'Male')], required=True, help="Animal gender")
    repro_stage = fields.Char(string='Reproductive Stage', size=50, required=True, help="Reproductive stage of the animal")
    birth_weight = fields.Float(string='Birth Weight', digits=(4, 2), required=True, help="Animal birth weight")
    born_date = fields.Date(string='Born Date', default=datetime.now(), required=True, help="Date of birth of the animal")
    labour_type = fields.Char(string='Labour Type', size=30, required=True, help="Type of birth of the animal")
    purchased = fields.Boolean(string='Purchased', default=False, help="Indicates when the animal has been purchased")
    sick = fields.Boolean(string='Sick', default=False, help="Indicates when the animal is sick")
    #### Hidden fields ####
    breeder = fields.Char(string='Breeder', size=25, required=False, help="Livestock breeder")
    raised = fields.Integer(string='Raised', required=False, help="Height of livestock considered from the heel of the front legs to the cross")
    condition = fields.Selection(string='Condition', selection=_condition_animal_selection, required=False, help="Body condition of animal")
    features = fields.Text(string='Features', required=False, help="Special features of the animal")
    ####     #####     ####
    corral_id = fields.Many2one('livestock.corral', string='Corral', ondelete='set null', index=True)
    female_parent_id = fields.Many2one('livestock.animal', string='Mother', ondelete='set null', index=True)
    male_parent_id = fields.Many2one('livestock.animal', string='Father', ondelete='set null', index=True)
    disease_ids = fields.One2many('livestock.disease', 'animal_id', string=None, copy=False)
    nutrition_ids = fields.One2many('livestock.nutrition', 'animal_id', string=None, copy=False)
    weighing_ids = fields.One2many('livestock.weighing', 'animal_id', string=None, copy=False)
    event_ids = fields.One2many('livestock.event', 'animal_id', string=None, copy=False)

