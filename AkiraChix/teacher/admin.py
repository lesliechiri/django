from django.contrib import admin
from .models import Teacher



class TeacherAdmin(admin.ModelAdmin):
	list_display =  ("registration_number","first_name","last_name","email")
	search_fields = ("registration_number","first_name","last_name","email")


admin.site.register(Teacher,TeacherAdmin)
# Register your models here.
