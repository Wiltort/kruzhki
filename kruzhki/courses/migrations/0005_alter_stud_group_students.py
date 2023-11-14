# Generated by Django 4.2.7 on 2023-11-14 15:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_lesson_stud_group_title_alter_stud_group_students_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud_group',
            name='students',
            field=models.ManyToManyField(limit_choices_to={'is_staff': False}, related_name='stud_groups', to=settings.AUTH_USER_MODEL, verbose_name='Обучающиеся'),
        ),
    ]