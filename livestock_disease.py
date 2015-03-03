# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api

class livestock_disease(models.Model):
    _name = 'livestock.disease'
    _description = "Livestock Disease model"
    _order = "name desc"

    # Fields of the Disease Model
    name =  fields.Char(string='Identifier', size=8, required=True, help="Identifier of the disease")
    created_date = fields.Datetime(string= 'Identifier Date', required=True, default=datetime.now(), help = 'Date at which the disease was identified')
    diagnostician = fields.Char(string='Diagnostician', require = True ,size=30, default = lambda self: self.env.user.name, help="Indicates the person who performed the diagnosis")
    exam = fields.Text(string='Medical Exams', required=True, help="Indicates which medical tests should be performed")
    observation = fields.Text(string='Observations', required=False, help="Observations about the disease")
    symptoms = fields.Text(string='Symptoms', required=True, help="Disease symptoms")
    veterinarian = fields.Char(string='Veterinarian', required=True, help="Attending veterinarian")
    exam_result = fields.Text(string='Exams Result', required=False, help="Results of the exams")
    treatment = fields.Text(string='Treatment', required=True, help="Aplied Treatment")
    animal_id = fields.Many2one('livestock.animal', string='Animal', ondelete='cascade', index=True)
    sanitary_protocol_ids = fields.One2many('livestock.sanitary.protocol', 'disease_id', copy = False)
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable disease record")
    

class livestock_sanitary_protocol(models.Model):
    _name = 'livestock.sanitary.protocol'
    _description = "Livestock Sanitary Protocol model"
    _order = "treatment_date desc"

    # Fields of the Sanitary Protocol Model
    treatment_applier = fields.Char(string='Treatment applier', required=True, help="Person who apply the treatment")
    treatment_supervisor = fields.Char(string='Treatment supervisor', required=True, help="Person who supervises the application of treatment")
    treatment_date = fields.Datetime(string= 'Treatment Date', required=True, default = datetime.now(), help = 'Date at which the disease was applied')
    observation = fields.Text(string='Observations', required=False, help="Observations about the treatment")
    disease_id = fields.Many2one('livestock.disease', string='Disease', ondelete='cascade', index=True)     
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable treatment record")

