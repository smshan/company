# Generated by Django 3.1.7 on 2021-04-17 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0012_auto_20210417_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
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
            name='skills',
        ),
        migrations.DeleteModel(
            name='team',
        ),
    ]