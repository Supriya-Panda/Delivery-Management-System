from django.db import models
from agents.models import Agent

class DispatchLog(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='dispatch_logs')
    date = models.DateField(auto_now_add=True)
    orders_assigned = models.IntegerField()
    total_distance = models.FloatField()  
    total_time = models.IntegerField()    
    earnings = models.FloatField()        
    compliance_flag = models.BooleanField(default=True)  

    def __str__(self):
        return f"DispatchLog for {self.agent.name} on {self.date}"

