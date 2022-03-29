# -*- coding: utf-8 -*-

from odoo import fields, models, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    day_of_birth = fields.Date(sring="Day Of Birth")
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ], required=True, default="other")
    image = fields.Binary(string="Image", attachment=True)
    health_status = fields.Text(string="Health Status", required=True)
    hospital_admission_date = fields.Date(string="Hospital Admission Date", required=True)
    hospital_discharge_date = fields.Date(string="Hospital Discharge Date")
    note = fields.Text(string="Description")
