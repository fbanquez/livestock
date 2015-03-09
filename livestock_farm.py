# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api, _

class livestock_farm(models.Model):
    _name = 'livestock.farm'
    _inherits = {'res.company': 'company_id'} 
    _description = "Livestock Farm model"
    _order = "key desc"

    def _production_farm_selection(self):
        return(('milk', "Milk"),
               ('dual', "Dual Purpose"),
               ('commercial', "Commercial Breeding"),
               ('fattening', "Fattening"))

    def on_change_country(self, cr, uid, ids, country_id, context=None):
        res = {'domain': {'state_id': []}}
        rate_obj = self.pool.get('res.currency.rate')
        rate_id = rate_obj.search(cr, uid, [('rate', '=', 1)], context=context)
        currency_id = rate_id and rate_obj.browse(cr, uid, rate_id[0], context=context).currency_id.id or False
        if country_id:
            currency_id = self.pool.get('res.country').browse(cr, uid, country_id, context=context).currency_id.id
            res['domain'] = {'state_id': [('country_id','=',country_id)]}
        res['value'] = {'currency_id': currency_id}
        return res

    def onchange_state(self, cr, uid, ids, state_id, context=None):
        if state_id:
            return {'value':{'country_id': self.pool.get('res.country.state').browse(cr, uid, state_id, context).country_id.id }}
        return {}

    # Fields of the Farm Model
    company_id = fields.Many2one('res.company', string='Company', ondelete='restrict', required=True)
    key =  fields.Char(string='Identifier', size=8, required=True, help="Identifier of the farm")
    owner = fields.Char(string='Owner', size=25, help="Owner of the farm")
    breeder_id = fields.Char(string='Breeder Id', size=8, help="Identifier of the breeder")
    breeder_name = fields.Char(string='Breeder Name', size=25, help="Name of the breeder")
    production = fields.Selection(string='Production', selection=_production_farm_selection, required=True, help="Farm Production System")
    hectares = fields.Float(string='Hectares', digits=(7, 2), required=True, help="Number of acres comprising the farm")
    corrals = fields.Integer(string='Corrals', required=True, help="Numbers of corrals into the farm")
    grass_area = fields.Float(string='Grass Area', digits=(5, 2), required=True, help="Percentage of land covered with grass farm")
    bush_area = fields.Float(string='Bush Area', digits=(5, 2), required=True, help="Percentage of land covered with bush farm")
    grass_prevalent = fields.Text(string='Grass Prevalent', required=False, help="Indicates the kind of dominant grass on the farm")
    bush_prevalent = fields.Text(string='Bush Prevalent', required=False, help="Indicates the kind of dominant bush on the farm")
    map_farm = fields.Char(string='Farm Map', required=False, help="Map of the farm")
    thermo_ids = fields.One2many('livestock.thermo', 'farm_id', copy=False)
    corral_ids = fields.One2many('livestock.corral', 'farm_id', copy=False)
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable farm record")

