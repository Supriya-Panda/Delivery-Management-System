from django.contrib import admin
from .models import Warehouse
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'latitude', 'longitude']
    search_fields = ['name', 'city']
    list_filter = ['city']

admin.site.register(Warehouse, WarehouseAdmin)
