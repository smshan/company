from django.shortcuts import render
from django.template.response   import TemplateResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from .models import employee,skills
# Create your views here.
def home(request):
    form = employee()
    return render(request,'enroll/base.html',{'form':form})