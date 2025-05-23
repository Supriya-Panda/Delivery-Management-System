from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Agent

def check_in_agent(request, agent_id):
    agent = get_object_or_404(Agent, id=agent_id)
    
    agent.check_in_time = timezone.now()
    agent.is_active = True
    agent.available_for_assignment = True
    agent.save()
    return JsonResponse({
        "message": f"{agent.name} checked in successfully.",
        "check_in_time": agent.check_in_time,
        "available": agent.available_for_assignment
    })
