from django.core.management.base import BaseCommand
from warehouses.models import Warehouse
from agents.models import Agent
from orders.models import Order
import random

class Command(BaseCommand):
    help = "Simple command to load sample data"

    def handle(self, *args, **kwargs):
        warehouses = []
        for i in range(10):
            wh = Warehouse.objects.create(
                name=f"Warehouse-{i+1}",
                city="TestCity",
                latitude=12.9 + i * 0.01,
                longitude=77.5 + i * 0.01
            )
            warehouses.append(wh)

        for wh in warehouses:
            for j in range(20):
                Agent.objects.create(
                    name=f"Agent-{wh.id}-{j+1}",
                    warehouse=wh
                )

        for wh in warehouses:
            for k in range(120):
                Order.objects.create(
                    warehouse=wh,
                    delivery_address=f"Address-{wh.id}-{k+1}",
                    latitude=wh.latitude + random.uniform(-0.01, 0.01),
                    longitude=wh.longitude + random.uniform(-0.01, 0.01),
                    distance_from_warehouse=random.uniform(1, 10),
                    estimated_delivery_time=random.randint(10, 60),
                    status="pending"
                )

        print("Sample data created: 10 Warehouses, 200 Agents, 1200 Orders")
