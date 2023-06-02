from django.contrib import admin
from .models import Rubric, Group, Schedule
# Register your models here.

class GrAdmin(admin.ModelAdmin):
    list_display = ('pk','name', 'price', 'rubric')
    list_display_links = ('name',)
    search_fields = ('name', 'rubric')

class RbAdmin(admin.ModelAdmin):
    list_display = ('pk','name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class ShAdmin(admin.ModelAdmin):
    list_display = ('pk','day', 'group', 'time')
    list_display_links = ('group',)
    search_fields = ('group',)

admin.site.register(Group, GrAdmin)
admin.site.register(Rubric, RbAdmin)
admin.site.register(Schedule, ShAdmin)