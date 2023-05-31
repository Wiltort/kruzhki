from django.db import models

#class Day()
# Create your models here.
class Rubric(models.Model):
    #направление кружка
    name = models.CharField(primary_key=True)


class Group(models.Model):
    name = models.CharField()
    #название кружка
    price = models.IntegerField()
    #week_lessons = models.PositiveSmallIntegerField(max = 30)
    id = models.AutoField(primary_key=True)
    rubric = models.ForeignKey(
        Rubric,
        on_delete=models.PROTECT,
        related_name = 'groups'
        )
    def __str__(self):
        return self.name

#расписание
class Schedule(models.Model):
    #группа
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name='schedule')
    #день недели. 0 - понедельник
    day = models.IntegerField(max = 6, min = 0)
    
