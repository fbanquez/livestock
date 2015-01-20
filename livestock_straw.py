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
    name = fields.Char(string='Name', size=25, required=True, select=True)
    key =  fields.Char(string='Identifier', size=8, required=True)
    color = fields.Char(string='Color', size=15, required=True)
    types = fields.Selection(string='Type', selection=_type_straw_selection, required=True)
    created_date = fields.Date(string='Created', default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), required=True)
    contents = fields.Char(string='Contents', size=25, required=True)
    responsible = fields.Char(string='Responsible', size=25, required=True)
    active = fields.Boolean(string='Active', default=True)

