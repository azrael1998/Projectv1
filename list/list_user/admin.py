from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import RegisterUserAppuser

@admin.register(RegisterUserAppuser)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password']
