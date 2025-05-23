from django.test import TestCase
from utils.payments import calculate_earnings, check_compliance

class ComplianceTests(TestCase):
    def test_compliance_pass(self):
        self.assertTrue(check_compliance(90, 550))  

    def test_compliance_fail_distance(self):
        self.assertFalse(check_compliance(110, 400))  

    def test_compliance_fail_time(self):
        self.assertFalse(check_compliance(80, 700))  

class EarningsTests(TestCase):
    def test_minimum_earning(self):
        self.assertEqual(calculate_earnings(10), 500)

    def test_earning_slab_25(self):
        self.assertEqual(calculate_earnings(30), 500 + 30 * 35)

    def test_earning_slab_50(self):
        self.assertEqual(calculate_earnings(55), 500 + 55 * 42)
