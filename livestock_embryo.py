# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api, _

class livestock_embryo(models.Model):
    _name = 'livestock.embryo'
    _description = "Livestock Embryo model"
    _order = "id desc"

    def _phase_embryo_selection(self):
        return(('mo', _("Morula")),
               ('cm', _("Compact Morula")),
               ('eab', _("Early Blastocyst")),
               ('exb', _("Expanded Blastocyst")),
               ('hb', _("Hatched Blastocyst")))

    def _quality_embryo_selection(self):
        return(('q1', _("Quality 1")),
               ('q2', _("Quality 2")),
               ('q3', _("Quality 3")),
               ('q4', _("Quality 4")))

    # Fields of the Embryo Model
    name = fields.Char(string='Identifier', size=8, required=True, select=True, help="Alphanumeric identifier embryo")
    species_id =  fields.Many2one(comodel_name='livestock.specie.animal', string='Species', required=True, ondelete='set null', help="Embryo species")
    race_id = fields.Many2one(comodel_name='livestock.race.animal', string='Race', required=True, ondelete='set null', help="Embryo race")
    mother = fields.Many2one('livestock.animal', string='Mother', ondelete='set null', index=True, domain=[('gender','=','female')], help="Female donor")
    father = fields.Many2one('livestock.animal', string='Father', ondelete='set null', index=True, domain=[('gender','=','male')], help="Male donor")
    phase = fields.Selection(string='Phase', selection=_phase_embryo_selection, required=True, help="Phase embryo")
    quality = fields.Selection(string='Quality', selection=_quality_embryo_selection, required=True, help="Quality embryo")
    embryo_date = fields.Date(string='Created', default=datetime.now(), required=True, help="Date of creation of the embryo")
    farm = fields.Char(string='Farm', size=25, help="Farm where the embryo was created")
    responsible = fields.Char(string='Responsible', size=25, required=True, default=lambda self: self.env.user.name, help="Biologist, veterinarian or person responsible for the creation of the embryo")
    straw_id = fields.Many2one('livestock.straw', string='Straw', ondelete='cascade', index=True)
    active = fields.Boolean(string='Active', default=True, help="Enable/Disable record")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
