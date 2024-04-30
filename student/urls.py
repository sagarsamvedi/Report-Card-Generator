from django.urls import path
from .views import *

urlpatterns = [
    path("",get_students, name='get_students'), 
    path("get_marks/<student_id>/",get_marks, name='get_student_marks'), 
]
