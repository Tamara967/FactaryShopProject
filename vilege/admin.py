from django.contrib import admin

# Register your models here.
from .models import Vilege


class VilegeAdmin(admin.ModelAdmin):
    list_display  = ('id', 'vilege_name')
    list_display_links = ('id', 'vilege_name')
    search_fields = ('id', 'vilege_name')

admin.site.register(Vilege, VilegeAdmin)
