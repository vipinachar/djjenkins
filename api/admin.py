from django.contrib import admin
from api.models import AppUser

@admin.register(AppUser)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password']
