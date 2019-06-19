from django.contrib import admin

# Register your models here.
from .models import Course, Faculty, Room

admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Room)
