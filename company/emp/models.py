from django.db import models

from django.forms import ModelForm, fields, TextInput, IntegerField

# Create your models here.


class skill(models.Model):
    skills=models.CharField(max_length=50)
    
class employee(models.Model):
    Roll=(
        ('D','Developer'),
        ('T','Tester')
        )
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=90)
    skill=models.ManyToManyField(skill)
    roll=models.CharField(max_length=1, choices=Roll )

class team(models.Model):
    team_name=models.CharField(max_length=50)
    emp_id=models.ForeignKey(employee,  on_delete=models.CASCADE)

class team_leader(models.Model):
    leader_name=models.CharField(max_length=50)
    emp_id=models.ForeignKey(employee, on_delete=models.CASCADE)





