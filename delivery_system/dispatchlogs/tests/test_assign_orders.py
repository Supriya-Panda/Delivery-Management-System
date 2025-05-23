from django.test import TestCase
from django.core.management import call_command
from warehouses.models import Warehouse
from agents.models import Agent
from orders.models import Order
from dispatchlogs.models import DispatchLog

class AssignOrdersCommandTestCase(TestCase):
    def setUp(self):
        self.warehouse = Warehouse.objects.create(
            name="Test Warehouse",
            city="Test City",
            latitude=12.9,
            longitude=77.5
        )

        self.agent = Agent.objects.create(
            name="Test Agent",
            warehouse=self.warehouse,
            is_active=True,
            available_for_assignment=True
        )

        for i in range(55):
            Order.objects.create(
                warehouse=self.warehouse,
                delivery_address=f"Test Address {i}",
                latitude=12.91,
                longitude=77.51,
                status="pending"
            )

    def test_assign_orders_and_postpone_remaining(self):
        call_command('assign_orders')

        assigned_orders = Order.objects.filter(assigned_agent=self.agent)
        self.assertEqual(assigned_orders.count(), 50)

        postponed_orders = Order.objects.filter(pending_next_day=True)
        self.assertEqual(postponed_orders.count(), 5)

        dispatch_log = DispatchLog.objects.filter(agent=self.agent).first()
        self.assertIsNotNone(dispatch_log)
        self.assertEqual(dispatch_log.orders_assigned, 50)

        print("✅ assign_orders command logic verified.")
