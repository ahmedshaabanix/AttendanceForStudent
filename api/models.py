# from django.db import models
# from accounts.models import MyUser
# # from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# # from django.utils import timezone
# # from django.utils.translation import ugettext_lazy as _

# # # Create your models here.

# # class CustomUserManager(BaseUserManager):
# #     """
# #     Custom user model manager where email is the unique identifiers
# #     for authentication instead of usernames.
# #     """
# #     def create_user(self, email, password,arabic_name,username, **extra_fields):
# #         """
# #         Create and save a User with the given email and password.
# #         """
# #         if not email:
# #             raise ValueError(_('The Email must be set'))
# #         email = self.normalize_email(email)
# #         user = self.model(email=email,password = password,arabic_name = arabic_name,username =username,**extra_fields)
# #         user.set_password(password)
# #         user.save()
# #         return user

# # class Student(AbstractBaseUser): 
# #     username = models.CharField(max_length= 255)
# #     arabic_name = models.CharField(max_length= 255)
# #     email = models.EmailField(unique = True)
# #     is_active = models.BooleanField(default= True)
# #     date_joined = models.DateTimeField(default=timezone.now)
# #     USERNAME_FIELD = 'username'
# #     REQUIRED_FIELD =['arabic_name',]

# #     objects =  CustomUserManager()



    

