# -*- coding: utf-8 -*-

from openerp import models, fields, api, _

class livestock_corral_wizard(models.TransientModel):
    _name = 'livestock.corral.wizard'

    identifier = fields.Char(string='Corral Identifier', 
                             help="Put here the alphanumeric corral identifier")
    gender = fields.Selection(string='Gender', 
                              selection=[('female', _("Female")), ('male', _("Male"))], 
                              required=True, help="Animal gender")
    status = fields.Char(string='Status', 
                         help="Put here the status of the animal")

    def corral_report_creator(self, cr, uid, ids, context=None):
        wizard_obj = self.read(cr, uid, ids, context=context)[0]
##        print wizard_obj
        corral_code = wizard_obj.get('identifier')
        animal_status = wizard_obj.get('status')


        context = dict(context)
        context.update({'code': corral_code, 'status': animal_status})

        return {
            'type': 'ir.actions.report.xml',
            'report_type':'qweb-html',
            'report_name': 'livestock.corral_report',
            'data': context,
        }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
