from django.db import models


#class Day()
# Create your models here.
class Rubric(models.Model):
    #направление кружка
    name = models.CharField(
        primary_key=True, max_length=20, db_index=True, 
        verbose_name = 'Направление',
        )
    


class Group(models.Model):
    name = models.CharField(max_length=50)
    #название кружка
    price = models.IntegerField()
    #week_lessons = models.PositiveSmallIntegerField(max = 30)
    id = models.AutoField(primary_key=True)
    rubric = models.ForeignKey(
        'Rubric',
        on_delete=models.PROTECT,
        related_name = 'groups',
        blank = True,
        null = True,
          
        )
    def __str__(self):
        return self.name

#расписание
class Schedule(models.Model):
    #группа
    DAYS = (
        (0, 'Понедельник'),
        (1, 'Вторник'),
        (2, 'Среда'),
        (3, 'Четверг'),
        (4, 'Пятница'),
        (5, 'Суббота'),
        (6, 'Воскресенье'),
        )
    group = models.ForeignKey(
        Group, on_delete = models.CASCADE, related_name='schedule',
        )
    #день недели. 0 - понедельник
    day = models.IntegerField(choices = DAYS)
    time = models.TimeField(auto_now=True)
    
    
