from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(StudentClass)
admin.site.register(AcademicTerm)
admin.site.register(Subject)
admin.site.register(AcademicSession)
admin.site.register(SiteConfig)

