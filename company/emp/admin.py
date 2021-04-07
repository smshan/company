from django.contrib import admin
from .models import employee,team,skill,EmpSkill
#Register your models here.
admin.site.register(employee)
admin.site.register(team)
admin.site.register(skill)
@admin.register(EmpSkill)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name','email','skill','roll')

