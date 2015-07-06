# -*- coding: utf-8 -*-

from openerp import api, models


class OffspringReport(models.AbstractModel):
    _name = 'report.livestock.offspring_report'

    @api.multi
    def render_html(self, data=None):
        report_obj = self.env['report']
        target_obj = self.env['livestock.animal']
        report = report_obj._get_report_from_name('livestock.offspring_report')

        #Ubico al animal con la referencia que viene del wizard
        search_subject = target_obj.search([('prod_id.default_code', '=', 
                                            data.get('identifier')) ])
        #Guardo el id del animal solicitado
        search_value = search_subject.id
        #Busco todos los animales cuyo id de progenitor coincidan con el id antes obtenido
        animal_obj = self.env['livestock.animal']
        selected_animals = animal_obj.search(['|', 
                                        ('female_parent_id', '=', search_value), 
                                        ('male_parent_id', '=', search_value)] )
        ##Llenar estructura que se envia al reporte con la crias del animal
        ids_to_print = []
        for animal in selected_animals:
            if animal.id:
                ids_to_print.append(animal.id)

        docargs = {
            'doc_ids': ids_to_print, 
            'doc_model': report.model, 
            'docs': selected_animals, 
        }

        return report_obj.render('livestock.offspring_report', docargs)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

