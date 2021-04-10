from django.shortcuts import render
from django.template.response   import TemplateResponse
from django.http import HttpResponse




from .models import employee,skills
# Create your views here.
def addemployee(request):
    if request.method == 'POST':
        fm=employee(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            sk=fm.cleaned_data['skill']
            rl=fm.cleaned_data['roll']
            reg= employee(name=nm,email=em,skill=sk,roll=rl)
            reg.save()
            fm=employee()
        else:
            fm=employee()
        emp=employee.objects.all()
        return render(request,'enroll/base.html',{'form':fm,'employee':emp})


    