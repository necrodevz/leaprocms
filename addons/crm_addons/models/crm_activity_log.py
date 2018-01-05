from odoo import models, fields, api

class Technichian (models.Model):
    _name = 'crm.activity.log'
    _inherit='crm.activty.log'

    technician_id = fields.Many2one('hr.employees', string="Technician")