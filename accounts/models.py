from django.db import models
from django.contrib.auth.models import (
 		BaseUserManager, AbstractBaseUser,PermissionsMixin
 	)
from django.contrib.auth.models import User
class MyUserManager(BaseUserManager):

    def get_by_natural_key(self, email):
        return self.get(email=email)


    # def create_user(self, username , email, password=None, is_active = True, is_doctor=False, is_student=False, is_superuser=False,is_staff = False):
    #     if not username:
    #         raise ValueError("Users must have username")
    #     if not email:
    #         raise ValueError("Users must have an email address")
    #     if not password:
    #         raise ValueError("Users must have a password")

    #     user_obj = self.model(
    #         username = username,
    #         email = self.normalize_email(email),
    #         password = password
            

    #     )
    #     #user = self.model(email=email,password = password,arabic_name = arabic_name,username =username,**extra_fields)
    #     user_obj.set_password(password) # change user password
    #     user_obj.is_student = is_student
    #     user_obj.is_superuser = is_superuser
    #     user_obj.is_doctor = is_doctor
    #     user_obj.save()
    #     return user_obj

    # def create_student_user(self, username ,email, password=None):
    #     user = self.create_user(
    #             username,
    #             email,
    #             password=password,
    #             is_active = True,
    #             is_student= True,
            
    #     )
    #     return user


    # def create_doctor_user(self,username, email, password=None):
    #     user = self.create_user(
    #             username,
    #             email,
    #             password=password,
    #             is_active = True,
    #             is_doctor=True,


            
    #     )
    #     return user
    # def create_stuffuser(self, username,email, password=None):
    #     user = self.create_user(
    #         username,
    #         email,
    #         password=password,
    #         is_staff= True
    #     )
    #     return user

    # def create_superuser(self, username,email, password=None):
    #     user = self.create_user(
    #             username,
    #             email,
    #             password=password,
    #             is_active = True,
    #             is_superuser=True
    #     )
    #     return user

class MyUser(AbstractBaseUser):

    username = models.CharField(max_length = 255, unique = True)
    email   = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=254, blank=True)
    last_name = models.CharField(max_length=254, blank=True)
    # timestamp   = models.DateTimeField(auto_now_add=True)
    # is_superuser       = models.BooleanField(default= False)
    # is_active = models.BooleanField(default=True,)
    # is_doctor = models.BooleanField(default= False)
    # is_student     = models.BooleanField(default= False) 
    # is_staff = models.BooleanField(default= False)
    objects = MyUserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []



    # @property
    # def is_doctor(self):
    #     return self.doctor

    # @property
    # def is_superuser(self):
    #     return self.superuser

    # @property
    # def is_student(self):
    #     return self.student
class StudentManager(BaseUserManager):
    def create_student_user(self, username, email  ,name, department,level,password = None):
        if not username:
            raise ValueError("Users must have username")
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        email = self.normalize_email(email)
        student = Student(
            username = username,
            email = email,
            name = name, 
            department = department,
            level = level,
            password = password
            
        )
        student.set_password(password)
        student.save()
        return student


class DoctorManager(BaseUserManager):

    def create_doctor_user(self, username, email , password = None):
        if not username:
            raise ValueError("Users must have username")
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        email = self.normalize_email(email)
        doctor = Doctor(
            username = username,
            email = email,
            password = password,
            
        )
        doctor.set_password(password)
        doctor.save()
        return doctor

class Doctor(MyUser):
    name = models.CharField(max_length = 255, null = True)


    objects = DoctorManager()
 
    def __str__(self):
        return self.name


class Student(MyUser):
    name = models.CharField(max_length = 255, null = True)
    department = models.CharField(max_length = 255, null = True)
    level = models.CharField(max_length = 20,null=True)

    objects = StudentManager()

    def __str__(self):
        return self.name