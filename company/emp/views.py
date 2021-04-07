from django.shortcuts import render
from django.template.response   import TemplateResponse
from django.http import HttpResponse
from.forms import employeeform
from .models import employee,skill
# Create your views here.
def add_show(request):
    if request.method =='POST':
        fm =employeeform(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            rl = fm.cleaned_data['roll']
            reg = employee(name=nm,email=em,roll=rl)
            reg.save()
    else:
        fm = employeeform()
    return render(request, 'enroll/addandshow.html',{'form':fm})