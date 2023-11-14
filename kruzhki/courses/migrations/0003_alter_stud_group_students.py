# Generated by Django 4.2.7 on 2023-11-14 14:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_stud_group_students_alter_stud_group_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud_group',
            name='students',
            field=models.ManyToManyField(null=True, related_name='stud_groups', to=settings.AUTH_USER_MODEL, verbose_name='Обучающиеся'),
        ),
    ]