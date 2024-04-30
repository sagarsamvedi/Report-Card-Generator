from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Sum


def get_students(request):
    students = Student.objects.all()
    search = request.GET.get('search')
    if search:
        students = Student.objects.filter(student_name__icontains = search)
    
    # to get data in random order
    # students = students.order_by('?')

    paginator = Paginator(students, 10)  # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)

    return render(request,'index.html',{"students" : page_obj})



def get_marks(request,student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    rank = ReportCard.objects.filter(student__student_id__student_id = student_id)


    total_marks_obtained = total_marks['total_marks']
    total_subjects = queryset.count()  # Total number of subjects
    total_possible_marks = total_subjects * 100  # Assuming each subject has a maximum of 100 marks
    percentage = (total_marks_obtained / total_possible_marks) * 100 if total_possible_marks else 0
    percentage = round(percentage, 2)  # Round to 2 decimal places
    


    return render(request, 'marks.html',{"queryset":queryset,'total_marks':total_marks,'rank':rank,'percentage':percentage})
