from django.contrib import admin
from .models import Endorsement

@admin.register(Endorsement)
class EndorsementAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
