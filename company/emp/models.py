from django.db import models
from django.forms import ModelForm

# Create your models here.
class employee(models.Model):
    Roll=(
        ('D','Developer'),
        ('T','Tester')
        )
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=90)
    skill=models.CharField(max_length=50)
    roll=models.CharField(max_length=1,choices=Roll)
 

class skills(models.Model):
    skills=models.ManyToManyField(employee)
    

   # class Meta:
    #    db_table = 'emp'

    #def __str__(self):
      #  return self.name


class team(models.Model):
    team_name=models.CharField(max_length=50)
    team_leader_id=models.ForeignKey(employee,  on_delete=models.CASCADE)




