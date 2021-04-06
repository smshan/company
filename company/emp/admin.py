from django.contrib import admin
from .models import employee,team,skill
# Register your models here.
admin.site.register(team)
admin.site.register(skill)
@admin.register(employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name','email','skill','roll')

