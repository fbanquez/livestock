# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.relativedelta import *
from openerp import api, models


class FatteningReport(models.AbstractModel):
    _name = 'report.livestock.fattening_report'

    @api.multi
    def render_html(self, data=None):
        report_obj = self.env['report']
        container_obj = self.env['livestock.farm']
        target_obj = self.env['livestock.animal']
        report = report_obj._get_report_from_name('livestock.fattening_report')

        #ubica el id de la finca
        farm_id = container_obj.search([('key', 'ilike', data.get('farm'))]).id
        
        #calculos para determinar la fecha actual menos la cantidad de meses
        months_14 = (datetime.today() - relativedelta(months=14)).date()
        months_16 = (datetime.today() - relativedelta(months=16)).date()

        query = """
            SELECT a.id
            FROM livestock_animal a INNER JOIN livestock_weighing w 
	            ON (a.id = w.animal_id AND w.current_weight BETWEEN 300 AND 320)
                INNER JOIN livestock_corral c 
                ON a.corral_id = c.id AND c.farm_id = %s 
            WHERE a.gender = 'male'
            AND a.born_date BETWEEN %s::date AND %s::date
            """
        terms = (farm_id, months_16, months_14,)
        self.env.cr.execute(query, terms)

        #ids de los animales machos que cumplen con el peso y la edad.
        ids_to_print = [row[0] for row in self.env.cr.fetchall()]

        #recordset con los animales que poseen los ids anteriores. 
        selected_animals = target_obj.browse(ids_to_print)
        print selected_animals

        docargs = {
            'doc_ids': ids_to_print, 
            'doc_model': report.model, 
            'docs': selected_animals, 
        }

        return report_obj.render('livestock.fattening_report', docargs)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

