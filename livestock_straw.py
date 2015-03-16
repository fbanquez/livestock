# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api, _

class livestock_straw(models.Model):
    _name = 'livestock.straw'
    _inherits = {'product.product': 'prod_id'} 
    _description = "Livestock Straw model"
    _order = "id desc"

    def _type_straw_selection(self):
        return(('nornal', _("Normal")),
               ('mini', _("Mini")))

    def _contents_straw_selection(self):
        return(('semen', _("Semen")),
                ('embryo', _("Embryo")))

    # Fields of the Straw Model
    prod_id = fields.Many2one('product.product', string='Parent', required=True, ondelete='cascade', select=True, auto_join=True)
    color = fields.Char(string='Color', size=15, required=True, help="Color of the straw")
    types = fields.Selection(string='Type', selection=_type_straw_selection, required=True, help="Typo of the straw")
    straw_date = fields.Date(string='Created', default=datetime.now(), required=True, help="Creation date of the straw")
    contents = fields.Selection(string='Contents', selection=_contents_straw_selection, required=True, help="Content of a straw")
    responsible = fields.Char(string='Responsible', size=25, required=True, default=lambda self: self.env.user.name, help="Biologist, veterinarian or person responsible for the creation of the straw")
    thermo_id = fields.Many2one('livestock.thermo', string='Thermo', ondelete='cascade', index=True)
    embryo_id = fields.Many2one('livestock.embryo', string='Embryo', ondelete='cascade', index=True)

