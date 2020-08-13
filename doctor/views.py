from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import socket
from .models import *
import pyqrcode
import png
from django.http import JsonResponse,HttpResponse
# from django.http import JsonResponse
# from .models import Attendance, exmaple

from  django.core import serializers



 
############## Generate QR ####################################################################
def generate_qr(request):

    host_name = socket.gethostname() 
    host_ip = socket.gethostbyname(host_name)
    password = request.POST['password']
    lecture_number = request.POST['lecture_number']
    
   
    # save subject in database
    subject = request.POST.get('subjects')

    usersubjects = Lecture_date(subject_id = int(subject),lecture_number = lecture_number).save()

    #lecture_id, department and level data 
    #values_list('id')[0][0] for returning an integer value not a QuerySet
    lecture_id = Lecture_date.objects.filter(subject_id = int(subject),lecture_number = lecture_number).values_list('id')[0][0]
    print(lecture_id)

    department = Departments.objects.filter(id = int(subject)).values_list('name')[0][0]
    print(department)

    level = Subjects.objects.filter(id = int(subject)).values_list('level')[0][0]
    print(level)
    
    # create qr
    qr_code_text =  password+ "&"+ host_ip+ "&" +str(lecture_id) + "&" + department + "&" + str(level)
      
    url = pyqrcode.create(qr_code_text)
    url.png('uca-url.png',scale= 40)
    url.show(scale=40)
    #save QR data in database
    qr_text = Qr_code( qr_code_text = qr_code_text )
    qr_text.save()
    return redirect('report')

#############################################################################################################


####### render html pages ###################################################################################
@login_required
def home(request):
    
    subjects = Subjects.objects.all()
    context = {
        'subjects' :subjects,
        'title':'home'
    }
    return render(request, 'doctor/home.html',context)


#@login_required
def report(request):
    return render(request, 'doctor/onetime_report.html',{'title':'report'})


@login_required
def final_reports(request):
    return render(request, 'doctor/final_reports.html',{'title':'reports'})

#############################################################################################################




########### show_attendance  ##################################################################################
from accounts.models import Student
from .models import Attendance
from django.views.decorators.http import require_http_methods
@login_required
@require_http_methods(["GET"])
def show_attendance(request):
    attendance = Attendance.objects.all()

    for student in attendance:
        if student.student_id and student.status == 1:
            student_attendnce = Student.objects.all().filter(id = student.student_id).values('id','name')
            print(student_attendnce)
    data = list(student_attendnce)

    return JsonResponse(data,safe=False)


@login_required
@require_http_methods(["GET"])
def show_absence(request):
    attendance = Attendance.objects.all()

    for student in attendance:
        if student.student_id and student.status == 0:
            student_absence = Student.objects.all().filter(id = student.student_id).values('id','name')
            print(student_absence)
    data = list(student_absence)

    return JsonResponse(data,safe=False)

### show All#################################

@login_required
@require_http_methods(["GET"])
def show_all(request):
    attendance = Student.objects.all()

    data = list(attendance)
    data = {
        'data' : data
    }

    return JsonResponse(data,safe=False)


