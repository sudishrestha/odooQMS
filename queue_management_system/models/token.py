from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date
import datetime 
import time
import calendar
import logging
_logger = logging.getLogger(__name__)

class qms_token(models.Model):
    _name = 'qms.token'
    department_id = fields.Many2one('hr.department', 'Department')
    doctor_id = fields.Many2one('hr.employee', 'Doctor')
    abbr=fields.Char(string='Abbreviation')
    startTime=fields.Char(string='Start Time',default="00:00")
    endTime=fields.Char(string='End Time',default="00:00")
    deptOpens=fields.Char(string='Department Opens',default="00:00")
    deptCloses=fields.Char(string='Department Closes',default="00:00")
    currentValue=fields.Integer(string='Current Value',default=0)
    maxValue=fields.Integer(string='Max Token',default=0)

    @api.multi
    def resetData(self):
        for item in self:
            raise UserError("Resetting data")
            # do something with selected records

class qms_token_detail(models.Model):
    _name = 'qms.token.detail'
    token_id = fields.Many2one('qms.token', 'Token')
    tokenValue=fields.Integer(string='Token Value',default=0)
    genertedTime=fields.Datetime(string='Generated Time')
    servedTime=fields.Datetime(string='Served Time')