from odoo import models, fields, api, _
import pandas
from datetime import date, datetime, timedelta


class AppraisalPeriod(models.Model):
    _name = "appraisal.period"
    _description = "Appraisal"

    name = fields.Char(string="Appraisal Period")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    employee_id = fields.Many2one('hr.employee')
    state = fields.Selection(
        [('inactive', 'Inactive'), ('active', 'Active'), ('close', 'Closed')],
        string='State', compute="compute_state")

    # period_value = fields.Integer(string="id")
    def compute_state(self):
        # self.state = 'active'
        today = date.today()
        for rec in self:
            if rec.start_date <= today <= rec.end_date:
                rec.state = 'active'
            elif today < rec.start_date:
                rec.state = 'inactive'
            elif today > rec.end_date:
                rec.state = 'close'


class period(models.Model):
    _name = "period"
    _description = "Appraisal"

    name = fields.Char(string="Name")
    period_id = fields.Many2one('appraisal.period', string="Appraisal Name")
    employee_id = fields.Integer(string="Employee")
    drop = fields.Boolean(string="Droped")
