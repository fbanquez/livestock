# -*- coding: utf-8 -*-

from openerp import api, models


class CorralContentReport(models.AbstractModel):
    _name = 'report.livestock.corral_report'

    @api.multi
    def render_html(self, data=None):
        report_obj = self.env['report']
        target_obj = self.env['livestock.corral']
        report = report_obj._get_report_from_name('livestock.corral_report')

        #Ubico el corral con el identificador provisto
        search_subject = target_obj.search([('code', 'ilike', 
                                            data.get('code')) ])
        ##Llenar estructura con el termo requerido
        ids_to_print = []
        if search_subject.id:
            ids_to_print.append(search_subject.id)

        docargs = {
            'doc_ids': ids_to_print, 
            'doc_model': report.model, 
            'docs': search_subject, 
        }

        return report_obj.render('livestock.corral_report', docargs)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

