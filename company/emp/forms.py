from django.core import validators
from django.forms import ModelForm
from django import forms
from emp.models import employee,skills
skill = [
    ('C', 'C'),
    ('C++', 'C++'),
    ('python', 'python'),
    ('java','java'),
    ('.Net','.Net'),
    ('HTML','HTML'),
    ('javascript','JS'),
    ('C#','C#'),
]

class EmployeeRegistration(forms.ModelForm):
       class Meta:
                 model = employee
                 fields =['name','email','skill','roll']
                 widgets = {
                     'name':forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
                     'email':forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
                     'skill':forms.SelectMultiple(attrs={'class':'form-select', 'id':'skillid'} ,choices=skill ),
                     'roll':forms.Select(attrs={'class':'form-select', 'id':'rollid'})
                 }



