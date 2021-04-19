# Generated by Django 3.1.7 on 2021-04-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='roll',
        ),
        migrations.AddField(
            model_name='employee',
            name='skill',
            field=models.ManyToManyField(to='emp.skill'),
        ),
        migrations.DeleteModel(
            name='emp_skill_team',
        ),
    ]
