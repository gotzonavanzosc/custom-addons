# -*- coding: utf-8 -*-
# (c) 2016 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    no_sexual_offenses = fields.Boolean(
        string='Negative certificate sexual offenses', default=True)
