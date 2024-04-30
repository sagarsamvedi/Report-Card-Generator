from faker import Faker
import random
from datetime import datetime
from student.models import *
from django.utils import timezone
from django.db.models import Sum

fake = Faker()


def generate_student_id(department):
    department_prefix = department.department_name[:3].upper()
    current_year = datetime.now().year
    count = Student.objects.filter(department=department).count()+1
    return f"{department_prefix}-{count}-{current_year}"

def generate_fake_student():
    student_name = fake.name()
    student_email = fake.email()
    student_age = random.randint(18, 25)
    student_address = fake.address()
    return student_name, student_email, student_age, student_address

def generate_fake_data():
    departments = Department.objects.all()
    for department in departments:

        for _ in range(random.randint(5, 10)):
            student_id = StudentID.objects.create(
                student_id=generate_student_id(department))
            student_data = generate_fake_student()
            student = Student.objects.create(
                student_id=student_id,
                department=department,
                student_name=student_data[0],
                student_email=student_data[1],
                student_age=student_data[2],
                student_address=student_data[3],
            )

def generate_student_marks():
    students = Student.objects.all()
    subjects = Subject.objects.all()

    for student in students:
        for subject in subjects:
            marks = random.randint(0, 100)
            studentmarks = SubjectMarks.objects.create(
                student=student, subject=subject, marks=marks)

def generate_rank():
    
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks','-student_age')

    i = 1
    for rank in ranks:
        ReportCard.objects.create(
            student = rank,
            rank = i
        )
        i += 1