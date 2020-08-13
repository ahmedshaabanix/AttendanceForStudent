from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from.models import Doctor
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def profile(request):
    return render(request, 'accounts/profile.html',{'title':'profile'})



#################################
#           register           #
################################
def register(request):
    return render(request,'accounts/register.html',{'title':'register'})


def register_handler(request):
    user = Doctor.objects.create_doctor_user(request.POST['username'],
                                    request.POST['email'],
                                    request.POST['password'])
    user.first_name = request.POST['first_name']                                  
    user.last_name = request.POST['last_name']    
    user.name = request.POST['name']
    user.save()                              
    return redirect('login')


#################################
#           login              #
################################


def log_in(request):
    return render(request,'accounts/login.html',{'title':'login'})


def login_handler(request):
    user_log =request.POST['username']
    password_log = request.POST['password']
    logged = authenticate(username = user_log , password = password_log)

    if logged is not None:
        login(request,logged)
        return redirect('home')
    else:
        return redirect('login')


#################################
#           logout             #
################################

def logout_handler(request):
    logout(request)
    return redirect('login')




