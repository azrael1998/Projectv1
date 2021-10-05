from django.contrib import admin
from .models import AppUser

@admin.register(AppUser)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password']
