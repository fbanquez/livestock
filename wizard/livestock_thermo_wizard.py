# -*- coding: utf-8 -*-

from openerp import models, fields, api, _

class livestock_thermo_wizard(models.TransientModel):
    _name = 'livestock.thermo.wizard'

    name_search = fields.Char(string='Name', 
                             help="Put here the alphanumeric thermo name")

    def thermo_report_creator(self, cr, uid, ids, context=None):
        wizard_obj = self.read(cr, uid, ids, context=context)[0]
##        print wizard_obj
        thermo_name = wizard_obj.get('name_search')


        context = dict(context)
        context.update({'thermo_name': thermo_name})

        return {
            'type': 'ir.actions.report.xml',
            'report_type':'qweb-html',
            'report_name': 'livestock.thermo_report',
            'data': context,
        }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
