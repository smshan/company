from django.shortcuts import render
from django.template.response   import TemplateResponse
from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
from .forms import EmployeeRegistration
from .models import employee
# Create your views here.
def addemployee(request):
    emp = employee.objects.all()
    fm = EmployeeRegistration()
    return render(request,'enroll/base.html',{'form':fm,'em': emp})
#@csrf_exempt
def save_data(request):
    form= EmployeeRegistration(request.POST)
    if request.method=="POST":
        if form.is_valid():
            name= request.POST['name']
            email = request.POST['email']
            skill = request.POST['skill']
            roll = request.POST['roll']
            usr = employee(name=name,email=email,skill=skill,roll=roll)
            form.save()
            emp = employee.objects.values()
            print(emp)
            employee_data = list(emp)
            return JsonResponse({'status' : 'save' ,'employee_data': employee_data})
        else:
            return JsonResponse({'status' : 0})
           
           
           
           
           
        