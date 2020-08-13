from django.contrib import admin
from.models import (
    Subjects,Departments
    )
# Register your models here.
#adding our models to admin site 
admin.site.register(Subjects)
admin.site.register(Departments)

