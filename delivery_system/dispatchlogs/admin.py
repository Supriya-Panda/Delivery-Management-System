from django.contrib import admin
from .models import DispatchLog

@admin.register(DispatchLog)
class DispatchLogAdmin(admin.ModelAdmin):
    list_display = ('agent', 'date', 'orders_assigned', 'total_distance', 'total_time', 'earnings', 'compliance_flag')