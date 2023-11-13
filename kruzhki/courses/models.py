from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Stud_Group(models.Model):
    name = models.CharField(verbose_name='Группа', unique=True, max_length=50)
    teacher = models.ForeignKey(User, on_delete=models.DO_NOTHING, 
                                related_name='stud_groups', verbose_name='Преподаватель')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    #teacher настроить на роль преподавателя
    #в модели учеников сделать ссылку на Группу
    # в модели предметы сделать ссылку
    #

#class Student(models.Model):


# Create your models here.
