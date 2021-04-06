from django.contrib import admin
from .models import employee,team,skill
# Register your models here.
admin.site.register(employee)
admin.site.register(team)

admin.site.register(skill)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name','email','roll')

