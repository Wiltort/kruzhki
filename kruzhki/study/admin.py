from django.contrib import admin
from .models import Rubric, Group, Schedule
# Register your models here.

admin.site.register(Group)
admin.site.register(Rubric)
admin.site.register(Schedule)