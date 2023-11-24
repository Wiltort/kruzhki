from rest_framework import serializers
from .models import Rubric, Stud_Group, Student, Lesson, Schedule


class RubricSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rubric
        fields = ('id', 'name', 'image', 'stud_groups')


class Stud_GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stud_Group
        fields = ('id', 'name', 'title', 'teacher', 'description', 
                  'number_of_lessons', 'rubric', 'students', 'lessons',
                  'schedule')
        

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'user', 'in_group', 'attending')


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'stud_group', 'date', 'topic', 'attending')


class ScheduleSerializer():
    
    class Meta:
        model = Schedule
        fields = ('id', 'group', 'day_of_week', 'duration', 'begin_at')