# Generated by Django 4.0.4 on 2022-05-05 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_alter_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True, verbose_name='Course year'),
        ),
    ]