from django.core import validators
from django.forms import ModelForm
from django import forms
from emp.models import employee,skill

class employeeform(forms.ModelForm):
    name = forms.TextInput(attrs={'class':'form-control'}),
    email =forms.EmailInput(attrs={'class':'form-control'}),
    skill=forms.ModelMultipleChoiceField(queryset=skill.objects.all(), required=False)
    roll=forms.Select(attrs={'class':'form-select'})
    class Meta:
        model = employee
        fields = ['name','email','roll']
        list_display = ('name','email','roll')
  
          


