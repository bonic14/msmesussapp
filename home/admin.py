from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# admin.site.register(Employees)

admin.site.register(SessionsModel)
@admin.register(Ihuzo)
class IhuzoAdmin(ImportExportModelAdmin):
    pass
