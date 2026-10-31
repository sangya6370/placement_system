from django.contrib import admin
from .models import Student,Company,PlacementDrive,Application

# Register your models here
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(PlacementDrive)
admin.site.register(Application)
