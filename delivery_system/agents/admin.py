from django.contrib import admin
from .models import Agent

class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'warehouse', 'is_active', 'available_for_assignment', 'max_working_hours', 'max_distance_per_day')
    list_filter = ('warehouse', 'is_active', 'available_for_assignment')
    search_fields = ('name',)

admin.site.register(Agent, AgentAdmin)
