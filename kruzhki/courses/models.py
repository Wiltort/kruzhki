from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

def validate_teacher(T):
    t = User.objects.get(id = T)
    if not t.is_staff:
        raise ValidationError(
            'Пользователь %(name) не является преподавателем', 
            code='has_no_permission',
            params={'name': T.username})


class Stud_Group(models.Model):
    name = models.CharField(verbose_name='Группа', unique=True, max_length=50)
    title = models.CharField(verbose_name='Название курса', max_length=150)
    teacher = models.ForeignKey(User, on_delete=models.DO_NOTHING, 
                                related_name='work_group', 
                                verbose_name='Преподаватель', 
                                limit_choices_to={'is_staff': True})
    description = models.TextField(verbose_name='Описание', 
                                   blank=True, null=True)
    students = models.ManyToManyField(User,
                                      verbose_name='Обучающиеся', 
                                      related_name='stud_groups',
                                      limit_choices_to={'is_staff': False},
                                      )
    #teacher настроить на роль преподавателя
    #в модели учеников сделать ссылку на Группу
    # в модели предметы сделать ссылку


#class lesson(models.Model):
#    stud_group = models.ForeignKey()

#class Student(models.Model):


# Create your models here.
