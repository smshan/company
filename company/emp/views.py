from django.shortcuts import render
from django.template.response   import TemplateResponse
from django.http import HttpResponse
from .models import employee,skills
# Create your views here.
def addemployee(request):
    emp = employee.objects.all()
    return render(request,'enroll/base.html',{'em':emp})


    