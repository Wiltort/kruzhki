from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

def validate_teacher(T: User):
    if not T.is_staff:
        raise ValidationError(
            'Пользователь %(name) не является преподавателем', 
            code='has_no_permission',
            params={'name': T.username})


class Stud_Group(models.Model):
    name = models.CharField(verbose_name='Группа', unique=True, max_length=50)
    teacher = models.ForeignKey(User, on_delete=models.DO_NOTHING, 
                                related_name='work_group', 
                                verbose_name='Преподаватель', 
                                validators=[validate_teacher])
    description = models.TextField(verbose_name='Описание', 
                                   blank=True, null=True)
    students = models.ManyToManyField(User, blank=True, null=True, 
                                      verbose_name='Обучающиеся', 
                                      related_name='stud_groups')
    #teacher настроить на роль преподавателя
    #в модели учеников сделать ссылку на Группу
    # в модели предметы сделать ссылку
    #

#class Student(models.Model):


# Create your models here.
