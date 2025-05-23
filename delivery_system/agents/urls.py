from django.urls import path
from .views import check_in_agent

urlpatterns = [
    path('check-in/<int:agent_id>/', check_in_agent, name='agent-check-in'),
]
