# Generated by Django 3.1.7 on 2021-04-17 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0014_employee_skills_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill',
            field=models.ManyToManyField(to='emp.employee'),
        ),
    ]