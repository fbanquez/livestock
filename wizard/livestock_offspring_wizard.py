# -*- coding: utf-8 -*-

from openerp import models, fields, api, _

class livestock_offspring_wizard(models.TransientModel):
    _name = 'livestock.offspring.wizard'

    identifier = fields.Char(string='Animal Identifier', 
                             help="Put here the alphanumeric animal identifier")

    def animal_report_creator(self, cr, uid, ids, context=None):
        wizard_obj = self.read(cr, uid, ids, context=context)[0]
##        print wizard_obj
        animal_id = wizard_obj.get('identifier')


        context = dict(context)
        context.update({'identifier': animal_id})

        return {
            'type': 'ir.actions.report.xml',
            'report_type':'qweb-html',
            'report_name': 'livestock.offspring_report',
            'data': context,
        }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
