from django.contrib import admin
from .models import *
from django.db.models import Sum


class SubjectMarksAdmin(admin.ModelAdmin):
        # Define the display fields for the admin list view
        list_display = ['student','subject','marks']

class ReportCardAdmin(admin.ModelAdmin):

    list_display = ['student','rank','total_marks','date_of_generation']
    ordering = ['rank']

    def total_marks(self,obj):
        
        subject_marks = SubjectMarks.objects.filter(student = obj.student)
        marks = subject_marks.aggregate(marks = Sum('marks'))
        return marks['marks']



admin.site.register(Student)
admin.site.register(StudentID)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(SubjectMarks,SubjectMarksAdmin)
admin.site.register(ReportCard,ReportCardAdmin)

