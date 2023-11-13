from django.contrib import admin
from .models import Stud_Group


class Stud_GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'teacher')
    search_fields = ('name', 'teacher')
    list_filter = ('teacher',)

admin.site.register(Stud_Group, Stud_GroupAdmin)