from django.contrib import admin
from .models import *

from csvexport.actions import csvexport
# Register your models here.
# admin.site.register(Employees)

admin.site.register(SessionsModel)
admin.site.register(Ihuzo)

