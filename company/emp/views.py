from django.shortcuts import render
from django.template.response   import TemplateResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import employee,skills
# Create your views here.
def addemployee(request):
    emp = employee.objects.all()
    return render(request,'enroll/base.html',{'em':emp})
@csrf_exempt
def save_data(request):
    if request.method=="POST":
        form= employee(request.POST)
        if form.is_valid():
            nm = request.POST["name"]
            em = request.POST["email"]
            sk = request.POST["skill"]
            rl = request.POST["roll"]
            data = employee(name=nm,email=em,skill=sk,roll=rl)
            data.save()
            return JsonResponse({'status' : 'save'})
        else:
            return JsonResponse({'status' : 0})


    