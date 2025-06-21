
from django.contrib import admin
from .models import Developer

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'linkedin_url')
