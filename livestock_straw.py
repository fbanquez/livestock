# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api

class livestock_straw(models.Model):
    _name = 'livestock.straw'
    _description = "Livestock Straw model"
    _order = "name desc"

    def _type_straw_selection(self):
        return(('nornal', "Normal"),
               ('mini', "Mini"))

    def _contents_straw_selection(self):
        return(('semen', 'Semen'),
                ('embryo', 'Embryo'))

    # Fields of the Straw Model
    name = fields.Char(string='Identifier', size=8, required=True, help="Identifier of the straw")
    appellation =  fields.Char(string='Name', size=25, required=True, select=True, help="Straw name")
    color = fields.Char(string='Color', size=15, required=True, help="Color of the straw")
    types = fields.Selection(string='Type', selection=_type_straw_selection, required=True, help="Typo of the straw")
    created_date = fields.Date(string='Created', default=datetime.now(), required=True, help="Creation date of the straw")
    contents = fields.Selection(string='Contents', selection=_contents_straw_selection, required=True, help="Content of a straw")
    responsible = fields.Char(string='Responsible', size=25, required=True, default=lambda self: self.env.user.name, help="Biologist, veterinarian or person responsible for the creation of the straw")
    thermo_id = fields.Many2one('livestock.thermo', string='Thermo', ondelete='cascade', index=True)
    embryo_id = fields.Many2one('livestock.embryo', string='Embryo', ondelete='cascade', index=True)
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable record")

