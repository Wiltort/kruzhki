from django.contrib import admin
from .models import Stud_Group
#from django.contrib.auth import get_user_model


#User = get_user_model()


class Stud_GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'title', 'teacher')
    search_fields = ('name', 'teacher')
    list_filter = ('teacher',)


#class StudentsAdmin(admin.ModelAdmin):
 #   list_display = ('pk', 'stud_group', 'work_group')



admin.site.register(Stud_Group, Stud_GroupAdmin)
#admin.site.register(User, StudentsAdmin)
