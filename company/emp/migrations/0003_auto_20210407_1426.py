# Generated by Django 3.1.7 on 2021-04-07 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emp', '0002_auto_20210407_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=90)),
                ('roll', models.CharField(choices=[('D', 'Developer'), ('T', 'Tester')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50)),
                ('team_leader_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmpSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empskill_email', to='emp.employee')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empskill_name', to='emp.employee')),
                ('roll', models.ForeignKey(choices=[('D', 'Developer'), ('T', 'Tester')], on_delete=django.db.models.deletion.CASCADE, related_name='empskill_roll', to='emp.employee')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empskill_skill', to='emp.skill')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='skill',
            field=models.ManyToManyField(to='emp.skill'),
        ),
    ]