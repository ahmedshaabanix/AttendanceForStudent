from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from accounts import views as user_views
from django.conf import settings


urlpatterns = [

    path('profile/',user_views.profile,name = 'profile'),
    path('',include('doctor.urls')),
    path('admin/', admin.site.urls,),

    # auth system
    path('register/',user_views.register , name = 'register'),
    path('register_handler/',user_views.register_handler,name ='register_handler'),
    path('login/', user_views.log_in, name='login'),
    path('login_handler/', user_views.login_handler, name='login_handler'),
    path('logout_handler/', user_views.logout_handler, name='logout_handler'),


    # password reset handling
    path('password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html'
        ),name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'
         ), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'
         ),name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'
         ),name='password_reset_complete'),

    # Rest_Api 
    path('', include('api.urls')),
    
]

