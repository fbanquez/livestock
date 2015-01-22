# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api

class livestock_straw(models.Model):
    _name = 'livestock.straw'
    _description = "Livestock Straw model"
    _order = "key desc"

    def _type_straw_selection(self):
        return(('no', "Normal"),
               ('mi', "Mini"))

    # Fields of the Straw Model
    name = fields.Char(string='Name', size=25, required=True, select=True, help="Straw name")
    key =  fields.Char(string='Identifier', size=8, required=True, help="Identifier of the straw")
    color = fields.Char(string='Color', size=15, required=True, help="Color of the straw")
    types = fields.Selection(string='Type', selection=_type_straw_selection, required=True, help="Typo of the straw")
    created_date = fields.Date(string='Created', default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), required=True, help="Creation date of the straw")
    contents = fields.Char(string='Contents', size=25, required=True, help="Content of a straw")
    responsible = fields.Char(string='Responsible', size=25, required=True, help="Biologist, veterinarian or person responsible for the creation of the straw")
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable record")

