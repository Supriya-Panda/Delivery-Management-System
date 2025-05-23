from django.db import models
from warehouses.models import Warehouse
from agents.models import Agent

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('delivered', 'Delivered'),
        ('postponed', 'Postponed'),
    )

    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='orders')
    delivery_address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    assigned_agent = models.ForeignKey(Agent, null=True, blank=True, on_delete=models.SET_NULL, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    distance_from_warehouse = models.FloatField(null=True, blank=True)  
    estimated_delivery_time = models.IntegerField(null=True, blank=True)  
    pending_next_day = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Order #{self.id} - {self.status}"
