# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.relativedelta import *
from openerp import models, fields, api, _

class livestock_animal(models.Model):
    _name = 'livestock.animal'
    _inherits = {'product.product': 'prod_id'} 
    _description = "Livestock Animal model"
    _order = "id, born_date desc"

    def _condition_animal_selection(self):
        return [(str(n), str(n)) for n in range(1, 10)]

    @api.one
    @api.depends('born_date')
    def _age_animal_compute(self):
        self.age = 0
        if self.born_date:
            today = datetime.now().date()
            bday = datetime.strptime(self.born_date, '%Y-%m-%d').date()
            rel = relativedelta(today, bday)
            self.age = str(rel.years) + " - " + str(rel.months) + " - " + str(rel.days)

    def _gestation_animal_selection(self):
        return(('mating', _("Natural Mating")),
               ('biotechnology', _("Biotechnology")))

    def _biotech_animal_selection(self):
        return(('insemination', _("Artificial Insemination")),
               ('flushing', _("Follicular Flushing")),
               ('aspiration', _("Follicular Aspiration")))

    def _labour_type_animal_selection(self):
        return(('normal', _("Normal")),
               ('caesarean', _("Caesarean Section")),
               ('induced', _("Induced")))

    def _repro_stage_selection(self):
        return(('proestrus', _("Proestrus")),
               ('estrus', _("Estrus")),
               ('metestrus', _("Metestrus")),
               ('diestrus', _("Diestrus")))

    @api.one
    def _get_image(self):
        return dict((s.id, tools.image_get_resized_images(s.image)) for s in self)

    @api.one
    def _set_image(self):
        return self.write({'image': tools.image_resize_image_big(value)})
        
    # Fields of the Animal Model
    prod_id = fields.Many2one('product.product', string='Parent', required=True, ondelete='cascade', select=True, auto_join=True)
    age = fields.Char(string='Age', size=15, copy=False, readonly=True, compute='_age_animal_compute', help="Age of the animal in [years - months - days] format")
    gestation = fields.Selection(string='Gestation', selection=_gestation_animal_selection, required=True, help="Type of gestation")
    biotech = fields.Selection(string='Biotechnology', selection=_biotech_animal_selection, required=False, help="Type of biotechnology that suitable gestation")
    registration = fields.Char(string='Registration', size=8, required=False, help="Identification of an animal to an association of farmers")
    gender = fields.Selection(string='Gender', selection=[('female', _("Female")), ('male', _("Male"))], required=True, help="Animal gender")
    birth_weight = fields.Float(string='Birth Weight', digits=(4, 2), required=True, help="Animal birth weight")
    born_date = fields.Date(string='Born Date', default=datetime.now(), required=True, help="Date of birth of the animal")
    labour_type = fields.Selection(string='Labour Type', required=True, selection=_labour_type_animal_selection, help="Type of birth of the animal")
    purchased = fields.Boolean(string='Purchased', default=False, help="Indicates when the animal has been purchased")
    sick = fields.Boolean(string='Sick', default=False, help="Indicates when the animal is sick")
    #### Hidden fields ####
    breeder = fields.Char(string='Breeder', size=25, required=False, help="Livestock breeder")
    raised = fields.Float(string='Raised', digits=(4, 2), required=False, help="Height of livestock considered from the heel of the front legs to the cross")
    condition = fields.Selection(string='Condition', selection=_condition_animal_selection, required=False, help="Body condition of animal")
    features = fields.Text(string='Features', size=500, required=False, help="Special features of the animal")
    ####     #####     ####
    specie_id = fields.Many2one(comodel_name='livestock.specie.animal', string='Specie', ondelete='set null', index=True)
    race_id = fields.Many2one(comodel_name='livestock.race.animal', string='Race', ondelete='set null', index=True)
    colour_id = fields.Many2one(comodel_name='livestock.color.animal', string='Color', ondelete='set null', index=True)
    status_id = fields.Many2one(comodel_name='livestock.status.animal', string='Status', ondelete='set null', index=True)
    corral_id = fields.Many2one(comodel_name='livestock.corral', string='Corral', ondelete='set null', index=True)
    female_parent_id = fields.Many2one(comodel_name='livestock.animal', string='Mother', ondelete='set null', index=True, domain=[('gender','=','female')])
    male_parent_id = fields.Many2one(comodel_name='livestock.animal', string='Father', ondelete='set null', index=True, domain=[('gender','=','male')])
    disease_ids = fields.One2many('livestock.disease', 'animal_id', string=None, copy=False)
    nutrition_ids = fields.One2many('livestock.nutrition', 'animal_id', string=None, copy=False)
    weighing_ids = fields.One2many('livestock.weighing', 'animal_id', string=None, copy=False)
    event_ids = fields.One2many('livestock.event', 'animal_id', string=None, copy=False)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
