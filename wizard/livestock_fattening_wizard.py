# -*- coding: utf-8 -*-

from openerp import models, fields, api, _

class livestock_fattening_wizard(models.TransientModel):
    _name = 'livestock.fattening.wizard'

    identifier = fields.Char(string='Farm Identifier', 
                             help="Put here the alphanumeric farm identifier")

    def fattening_report_creator(self, cr, uid, ids, context=None):
        wizard_obj = self.read(cr, uid, ids, context=context)[0]
##        print wizard_obj
        farm_id = wizard_obj.get('identifier')


        context = dict(context)
        context.update({'farm': farm_id})

        return {
            'type': 'ir.actions.report.xml',
            'report_type':'qweb-html',
            'report_name': 'livestock.fattening_report',
            'data': context,
        }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
