from django.core import validators
from django import forms
from .models import employee

class employeeform(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['name','email','skill','roll']
        widgets = {
               'name' : forms.TextInput(attrs={'class':'form-control'}),
               'email' : forms.EmailInput(attrs={'class':'form-control'}),
               'skill':forms.TextInput(attrs={'class':'form-control'}),
               'roll':forms.Select(attrs={'class':'form-select'}),
            
        }
   



