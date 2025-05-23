from django.test import TestCase
from utils.geo import haversine_distance

class HaversineDistanceTest(TestCase):
    def test_same_location(self):
        d = haversine_distance(19.0760, 72.8777, 19.0760, 72.8777)
        self.assertAlmostEqual(d, 0.0, places=2)

    def test_known_distance(self):
        mumbai = (19.0760, 72.8777)
        pune = (18.5204, 73.8567)
        d = haversine_distance(*mumbai, *pune)
        self.assertTrue(120 < d < 160)  