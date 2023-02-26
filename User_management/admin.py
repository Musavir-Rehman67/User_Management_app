from django.contrib import admin
from .models import UserRegistration

# Register your models here.
class AdminUserRegistration(admin.ModelAdmin):
    list_display = ['name','email_id','qualification',"address"]

admin.site.register(UserRegistration,AdminUserRegistration)