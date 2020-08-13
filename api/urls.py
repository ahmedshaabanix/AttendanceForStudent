from django.urls import path,include
from api.views import( RegisterAPI,
                          UserAPI,
                          LoginAPI,
                          student_attendance,
                          qr_match,
                          )
from knox import views as knox_views
#from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
  # authentication for student with knox 
  path('api/auth', include('knox.urls')),
  path('api/auth/register', RegisterAPI.as_view()),
  path('api/auth/login', LoginAPI.as_view()),
  path('api/auth/user', UserAPI.as_view()),
  path('api/auth/logout', knox_views.LoginView.as_view(), name='knox_logout'),
  
  # QR match and Attendance fro student
  path('api/qr' , qr_match, name = 'qr_match_api'),
  path('api/attendance',student_attendance, name = 'attendance_apis'),



]
