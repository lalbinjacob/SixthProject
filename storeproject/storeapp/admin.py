from django.contrib import admin

from storeapp.models import Department, Course, Ordering, Purpose

# Register your models here.

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Ordering)
admin.site.register(Purpose)

