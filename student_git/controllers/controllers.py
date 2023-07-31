# -*- coding: utf-8 -*-
# from odoo import http


# class StudentGit(http.Controller):
#     @http.route('/student_git/student_git/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/student_git/student_git/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('student_git.listing', {
#             'root': '/student_git/student_git',
#             'objects': http.request.env['student_git.student_git'].search([]),
#         })

#     @http.route('/student_git/student_git/objects/<model("student_git.student_git"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student_git.object', {
#             'object': obj
#         })
