from django.db import models

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department_name

    class Meta:
        ordering = ['department_name']

class StudentID(models.Model):

    student_id = models.CharField(max_length=100)

    def __str__(self):
        return self.student_id
    class Meta:
        ordering = ['student_id']
    
class Student(models.Model):
    student_id = models.OneToOneField(StudentID, related_name='studentid', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='department',on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=254, unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self):
        return self.student_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student,related_name='studentmarks', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    class Meta:
        # ensure that no there is no duplicate row with same student and subject
        unique_together = ['student','subject']
        verbose_name_plural = 'student marks'
    
    def __str__(self):
        return f'{self.student.student_name} - {self.subject.subject_name}'

class ReportCard(models.Model):
    
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='studentreportcard')
    rank = models.IntegerField()
    date_of_generation = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['student','date_of_generation']