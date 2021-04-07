from django.core import validators
from django.forms import ModelForm
from django import forms
from emp.models import employee,skill,EmpSkill

class employeeform(forms.ModelForm):
    class Meta:
        model = EmpSkill
        fields = ['name','email','skill','roll']
     
      
        widgets = {
               'name' : forms.TextInput(attrs={'class':'form-control'}),
               'email' : forms.EmailInput(attrs={'class':'form-control'}),
               'skill':forms.TextInput(attrs={'class':'form-control'}),
               'roll':forms.Select(attrs={'class':'form-select'}),
            
        }
   

