from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    
    list_display=('title','description','is_completed')
    search_fields =('title','description','is_completed')
    list_per_page=25

admin.site.register(Todo,TodoAdmin)
