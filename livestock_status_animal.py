# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api, _

class livestock_status_animal(models.Model):
    _name = 'livestock.status.animal'
    _description = "Livestock Configuration States Animal Model"
    _order = "name"

    # Fields of the Configuration Animal Model
    name = fields.Char(string='State', index=True, required=True, help="Animal state")
    gender = fields.Selection(string='Gender', selection=[('female', _("Female")), ('male', _("Male"))], required=False, help="Animal gender")
    description = fields.Text(string='Description', size=500, help="Long description of the animal characteristic")
    animal_id = fields.One2many('livestock.animal', 'status_id', copy=False)
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable features record")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
