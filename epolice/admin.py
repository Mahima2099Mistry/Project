from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(User)
# admin.site.register(FIR)
admin.site.register(Criminal)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','role']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email']

@admin.register(FIR)
class FIRAdmin(admin.ModelAdmin):
    list_display = ['name','fir_title','status']