# Generated by Django 3.1.7 on 2021-04-09 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0007_auto_20210408_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='skill',
        ),
        migrations.AddField(
            model_name='employee',
            name='skill',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='skills',
            name='skills',
        ),
        migrations.AddField(
            model_name='skills',
            name='skills',
            field=models.ManyToManyField(to='emp.employee'),
        ),
        migrations.AlterModelTable(
            name='employee',
            table=None,
        ),
    ]
