from django.contrib import admin
from .models import Programms

class ProgrammAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'download_link')

admin.site.register(Programms, ProgrammAdmin)
