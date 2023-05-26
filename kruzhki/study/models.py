from django.db import models

#class Day()
# Create your models here.
class Rubric(models.Model):
    name = models.CharField(primary_key=True)

class Group(models.Model):
    name = models.CharField()
    #название кружка
    price = models.IntegerField()
    week_lessons = models.PositiveSmallIntegerField(max = 30)
    id = models.AutoField(primary_key=True)
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT)

class Schedule(models.Model):
    gr_id = models.ForeignKey(Group, on_delete = models.CASCADE)