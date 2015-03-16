# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api, _

class livestock_weighing(models.Model):
    _name = 'livestock.weighing'
    _description = "Livestock Weighing Model"
    _order = "animal_id, weighing_date desc"

    @api.one
    @api.depends('animal_id', 'current_weight')
    def _daily_gain_compute(self):
        self.daily_gain = 0.00
        if self.animal_id.id:
            self.env.cr.execute("SELECT weighing_date, current_weight FROM livestock_weighing WHERE animal_id = %s AND weighing_date <= to_timestamp('%s','YYYY-MM-DD HH24:MI:SS') AND active ORDER BY weighing_date desc" % (self.animal_id.id, self.weighing_date))
            reg = self.env.cr.fetchall()
            if len(reg) > 1:
                diff = datetime.strptime(reg[1][0], '%Y-%m-%d %H:%M:%S') - datetime.strptime(reg[0][0], '%Y-%m-%d %H:%M:%S')
                self.daily_gain = (float(reg[1][1]) - float(reg[0][1]))/(1 if diff.days == 0 else diff.days)

    @api.one
    @api.depends('animal_id', 'current_weight')
    def _life_gain_compute(self):
        self.life_gain = 0.00
        if self.animal_id.id:
            self.env.cr.execute("SELECT birth_weight, born_date FROM livestock_animal WHERE id = %s" % (self.animal_id.id))
            reg = self.env.cr.fetchall()[0]
            if reg:
                diff = datetime.strptime(self.weighing_date,'%Y-%m-%d %H:%M:%S') - datetime.strptime(reg[1], '%Y-%m-%d')
                self.life_gain = (self.current_weight - float(reg[0]))/(1 if diff.days == 0 else diff.days)

    @api.one
    @api.depends('animal_id', 'projecting_days')
    def _weight_compute(self):
        self.adjusted_weight = 0.00
        if self.animal_id.id:
            self.env.cr.execute("SELECT birth_weight, born_date FROM livestock_animal WHERE id = %s" % (self.animal_id.id))
            reg = self.env.cr.fetchall()[0]
            if reg:
                diff = datetime.strptime(self.weighing_date,'%Y-%m-%d %H:%M:%S') - datetime.strptime(reg[1], '%Y-%m-%d')
                self.adjusted_weight = (((self.current_weight - float(reg[0]))/(1 if diff.days == 0 else diff.days)) * self.projecting_days) + float(reg[0])

    # Fields of the Weighing Model
    name = fields.Char(string='Identifier', size=8, required=True, help="Identifier of the Weighing")
    current_weight = fields.Float(string='Current Weight', digits=(6, 2), required=True, help="Current animal weight")
    weighing_date = fields.Datetime(string='Date', required=True, default=datetime.now(), help="Date on which the weight event occurred")
    daily_gain = fields.Float(string='Daily Gain', digits=(5, 2), readonly=True, compute='_daily_gain_compute', help="Daily weight gain of the animal")
    life_gain = fields.Float(string='Life Gain', digits=(5, 2), readonly=True, compute='_life_gain_compute', help="Grams profit animal life")
    projecting_days = fields.Integer(string='Projecting Days', required=True, default=0, help="Projected number of days")
    adjusted_weight = fields.Float(string='Adjusted Weight', digits=(6, 2), compute='_weight_compute', readonly=True, help="Animal weight set")
    responsible = fields.Char(string='Responsible', required=True, size=30, default=lambda self: self.env.user.name, help="Person who made the weigh")
    comment = fields.Text(string='Comment', required=False, help="Comments about weighing the animal")
    animal_id = fields.Many2one('livestock.animal', string='Animal', ondelete='cascade', index=True)
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable weighing record")

