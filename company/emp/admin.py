from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import employee,team,skills
from emp.forms import EmployeeRegistration

#Register your models here.

admin.site.register(team)
admin.site.register(skills)
admin.site.unregister(skills)
@admin.register(employee,skills)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email','get_skills','roll')

def get_skills(self,obj):
    return ", ".join([str(p) for p in self.skills.all()])