# Generated by Django 3.1.7 on 2021-04-07 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0003_auto_20210407_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empskill',
            name='email',
        ),
        migrations.RemoveField(
            model_name='empskill',
            name='name',
        ),
        migrations.RemoveField(
            model_name='empskill',
            name='roll',
        ),
        migrations.RemoveField(
            model_name='empskill',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='team',
            name='team_leader_id',
        ),
        migrations.DeleteModel(
            name='employee',
        ),
        migrations.DeleteModel(
            name='EmpSkill',
        ),
        migrations.DeleteModel(
            name='skill',
        ),
        migrations.DeleteModel(
            name='team',
        ),
    ]
