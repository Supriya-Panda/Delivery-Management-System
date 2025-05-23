from django.db import models
from warehouses.models import Warehouse
from django.utils import timezone

class Agent(models.Model):
    name = models.CharField(max_length=100)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='agents')
    check_in_time = models.DateTimeField(null=True, blank=True)
    max_working_hours = models.FloatField(default=10.0)
    max_distance_per_day = models.FloatField(default=100.0)
    is_active = models.BooleanField(default=False)
    available_for_assignment = models.BooleanField(default=False)
    def check_in(self):
        self.check_in_time = timezone.now()
        self.is_active = True
        self.save()

    def __str__(self):
        return self.name



