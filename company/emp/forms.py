from django.core import validators
from django import forms
from .models import employee

class EmployeeRegister(forms.ModelForm):
    class Meta:
        model=employee
        fields=['name','email','roll']