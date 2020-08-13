from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('reports/', views.final_reports, name = 'final_reports'),
    path('generate_qr/', views.generate_qr , name = 'generate_qr'),
    path('report/', views.report , name = 'report'),
    # show Attendance
    path('show_attendance/', views.show_attendance, name = "show_attendance" ),
    path('show_absence/', views.show_absence, name = "show_absence" ),
    path('show_all/', views.show_all, name = "show_all" ),



 

]