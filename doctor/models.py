from django.db import models
from django.utils import timezone

from accounts.models import Doctor





#  save the lecture data number and subject
class Lecture_date(models.Model):
    subject_id = models.IntegerField(null = True)
    lecture_number = models.IntegerField(null = True)
    date = models.DateTimeField(auto_now_add=True)
    



class Attendance(models.Model):
    lecture_date_id = models.IntegerField(null= True)
    student_id = models.IntegerField(null = True)
    status = models.IntegerField(null = True)
    class Meta:
        unique_together = ('lecture_date_id', 'student_id')


 


class Qr_code(models.Model):
    qr_code_text = models.CharField(max_length = 255)



class Departments(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


class Subjects(models.Model):
    name = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete= models.DO_NOTHING,null = True)
    level = models.IntegerField()
    department  =models.ForeignKey(Departments, on_delete= models.CASCADE ,null = True)

    
    def __str__(self):
        return self.name
