from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display=('username','email','is_staff')
    search_fields =('username','email','is_staff')
    list_per_page=25
    

admin.site.register(User, UserAdmin)
