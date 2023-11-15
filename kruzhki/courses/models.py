from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class Stud_Group(models.Model):
    name = models.CharField(verbose_name='Группа', unique=True, max_length=50)
    title = models.CharField(verbose_name='Название курса', max_length=150)
    teacher = models.ForeignKey(User, on_delete=models.PROTECT, 
                                related_name='groups', 
                                verbose_name='Преподаватель', 
                                limit_choices_to={'is_staff': True})
    description = models.TextField(verbose_name='Описание', 
                                   blank=True)
    

class Student(models.Model):
    user = models.ForeignKey(User, related_name='study',
                             limit_choices_to={'is_staff': False})
    in_group = models.ForeignKey(Stud_Group, related_name='students')


class Lesson(models.Model):
    stud_group = models.ForeignKey(Stud_Group, related_name='lessons',
                                   verbose_name='Занятия', 
                                   on_delete=models.PROTECT)
    date = models.DateTimeField(verbose_name='Время и дата')
    topic = models.CharField(max_length=150)
    

class Attending(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='attending', 
                               on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='attending')
    is_present = models.BooleanField(verbose_name='Посещение')
    is_passed = models.BooleanField(verbose_name='Зачет')


class Schedule(models.Model):
    group = models.ForeignKey(Stud_Group, related_name='Расписание')
    #day_of_week = models.Ch