from django.core.management import call_command
from django.test import TestCase
from warehouses.models import Warehouse
from agents.models import Agent
from orders.models import Order

class LoadDataCommandTestCase(TestCase):
    def test_load_data_command_creates_sample_data(self):
        call_command('load_data')
        self.assertEqual(Warehouse.objects.count(), 10)
        self.assertEqual(Agent.objects.count(), 200)
        self.assertEqual(Order.objects.count(), 1200)
        pending_orders = Order.objects.filter(status="pending").count()
        self.assertEqual(pending_orders, 1200)

        print("✅ load_data command test passed.")
