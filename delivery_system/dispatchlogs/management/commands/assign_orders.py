from django.core.management.base import BaseCommand
from warehouses.models import Warehouse
from agents.models import Agent
from orders.models import Order
from dispatchlogs.models import DispatchLog
from utils.geo import haversine_distance
from datetime import datetime
from utils.payments import calculate_earnings,check_compliance


MAX_ORDERS = 50
MAX_DISTANCE = 100  
MAX_TIME = 600  
TIME_PER_KM = 5  

class Command(BaseCommand):
    help = "Assign orders to agents while respecting delivery constraints"

    def handle(self, *args, **kwargs):
        today = datetime.today().date()
        Order.objects.filter(pending_next_day=True, assigned_agent__isnull=True).update(pending_next_day=False)
        print("✅ Reset previous day's postponed orders")
        for warehouse in Warehouse.objects.all():
            agents = Agent.objects.filter(warehouse=warehouse, is_active=True, available_for_assignment=True)
            orders = Order.objects.filter(warehouse=warehouse, assigned_agent__isnull=True,pending_next_day=False).order_by('id')

            if not agents or not orders:
                continue

            warehouse_lat, warehouse_lng = warehouse.latitude, warehouse.longitude
            order_queue = list(orders)


            for agent in agents:
                total_km = 0
                total_time = 0
                assigned_orders = []

                while order_queue and len(assigned_orders) < MAX_ORDERS:
                    order = order_queue[0]
                    distance = haversine_distance(warehouse_lat, warehouse_lng, order.latitude, order.longitude)
                    travel_time = distance * TIME_PER_KM

                    if total_km + distance > MAX_DISTANCE or total_time + travel_time > MAX_TIME:
                        break

                    order.assigned_agent = agent
                    order.distance_from_warehouse = round(distance, 2)
                    order.estimated_delivery_time = round(travel_time, 2)
                    order.status = 'assigned'
                    order.save()

                    assigned_orders.append(order)
                    total_km += distance
                    total_time += travel_time
                    order_queue.pop(0)

                DispatchLog.objects.create(
                    agent=agent,
                    orders_assigned=len(assigned_orders),
                    date=datetime.today().date(),
                    total_distance=round(total_km, 2),
                    total_time=round(total_time, 2),
                    earnings=calculate_earnings(len(assigned_orders)),
                    compliance_flag = check_compliance(total_km, total_time),
                )

                print(f"{agent.name} assigned {len(assigned_orders)} orders")
            
            for remaining_order in order_queue:
                remaining_order.pending_next_day = True
                remaining_order.save()
            print(f"⚠️ {len(order_queue)} orders postponed to next day for warehouse {warehouse.name}")
