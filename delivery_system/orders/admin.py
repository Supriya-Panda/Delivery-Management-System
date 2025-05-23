
from django.contrib import admin
from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'warehouse', 'delivery_address', 'status', 'assigned_agent', 'pending_next_day')
    list_filter = ('warehouse', 'status', 'pending_next_day')
    search_fields = ('delivery_address',)

admin.site.register(Order, OrderAdmin)
