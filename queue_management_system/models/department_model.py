from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date
import datetime 
import time
import calendar
import logging
_logger = logging.getLogger(__name__)

class qms_department(models.Model):
    _name = 'hr.department'
    _inherit = 'hr.department'
    deptOpen = fields.Datetime(string='Department Open', index=True, help="Time on which department opens.")
    deptCloses = fields.Datetime(string='Department Closes', index=True, help="Time on which department closes.")
   