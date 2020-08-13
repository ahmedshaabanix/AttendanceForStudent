from rest_framework import  generics, permissions
from rest_framework.response import Response
from.serializers import (UserSerializer,
                        RegisterSerializer,
                        LoginSerializer,
                        Qr_Serializers,
                        Attendance_Serializer
                        )
from knox.models import AuthToken
from doctor.models import Qr_code,Attendance

# Register API#######################################################

class RegisterAPI(generics.GenericAPIView):
  #include Serializer class
  serializer_class = RegisterSerializer
  def post(self, request, *args, **kwargs):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })

# Login API ########################################################
from django.contrib.auth import login as django_login

class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer
  def post(self, request,*args,**kwargs):
      serializer = LoginSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      user = serializer.validated_data["user"]
      django_login(request, user)
      return Response({
        "token":AuthToken.objects.create(user)[1]
      })

# Get User API
class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user




# for Matching QR ####################################################
from accounts.models import Student,MyUser
from doctor.models import Qr_code
from rest_framework.decorators import api_view

@api_view(['POST','GET'])
def qr_match(request):
    
    student_id = request.data['id']
    qr = request.data['qr_code_text']
    response = {}
    if student_id and qr:
      student = MyUser.objects.filter(id = student_id).count()
      print(student)
      qr_code_text = Qr_code.objects.filter(qr_code_text = qr).count()

      if qr_code_text:
        response['success'] = 2
        response['message'] = 'done'
      else:
        response['success'] = 1
        response['message'] = 'fail'
    else:
        response['success'] = 0
        response['message'] = 'No Data Recieved'
    return Response(response)





# for recording student attendance #####################################
from doctor.models import Lecture_date , Attendance
# Attendance API
@api_view(['POST',])
def student_attendance(request):
  student_id = request.data['id']
  lecture_date_id = request.data['lecture_date_id']
  department = request.data['department']
  level = request.data['level']
  response = {}
  # get all student id (return all student id inside <QuerySet [1, 4,....]>)#
  student_obj = Student.objects.all().filter(department =department,level =level)
       
  if student_id and lecture_date_id:

    for student in student_obj:
    
      try:
        if student.id == int(student_id) and lecture_date_id == lecture_date_id:
          query = Attendance.objects.filter(lecture_date_id=lecture_date_id,student_id= student_id).count()
        
          if query:
            response['success'] = 1
            response['message'] = 'Already registred'
          else:
            student_attend = Attendance(lecture_date_id =lecture_date_id,student_id = student_id, status = 1).save()
            response['success'] = 2
            response['message'] = 'ATTEND'

        else:
            student_absence = Attendance(lecture_date_id =lecture_date_id,student_id = student.id, status = 0).save()
            response['success'] = 3
            response['message'] = 'Done' 

      except:
        response['success'] = 4
        response['message'] = 'Data Already Exist!' 
  else:
    response['success'] = 0 
    response['message'] = 'No Data Recieved'
  return Response(response)








# @api_view(['POST',])
# def attendance(request):
#   student_id = request.data['id']
#   lecture_date_id = request.data['lecture_date_id']
#   print(student_id)
#   print(lecture_date_id)

#   response = {}
#   if  student_id  and lecture_date_id:
#     print(student_id)
#     print(lecture_date_id)

#     query = Attendance.objects.filter(lecture_date_id=lecture_date_id,student_id = student_id)
#     print(query)

#     if query:

#       response['success'] = 1
#       response['message'] = 'Already registred'
#     else:
#       student_attend = Attendance(lecture_date_id =lecture_date_id,student_id = student_id, status = 1).save()
#       response['success'] = 2
#       response['message'] = 'Done'
#   else:
#     response['success'] = 0
#     response['message'] = 'No Data Recieved'
#   return Response(response)
