# -*- coding: utf-8 -*-

from odoo import models, fields, api


class student(models.Model):
    _name = 'company.student_git'
    _description = 'company.student_git'

    name = fields.Char(string = "Name")
    age = fields.Integer(string = "Age")
    Class = fields.Char(string = "Class")

   