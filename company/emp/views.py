from django.shortcuts import render
from django.template.response   import TemplateResponse
from django.http import HttpResponse
from.forms import EmployeeRegister

# Create your views here.
def add_show(request):
    if request.method =='POST':
        fm = EmployeeRegister(request.POST)
    else:
        fm = EmployeeRegister()
    return render(request, 'enroll/addandshow.html',{'form':fm})
