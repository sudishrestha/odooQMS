from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date
import datetime 
import time
import calendar
import logging
_logger = logging.getLogger(__name__)

class qms_doctor(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    subtitle=fields.Char(string='Subtitle')
    nmcno=fields.Char(string='NMC no')

