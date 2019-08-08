from unittest import TestCase
from smallest_temp_spread import smallest

class SmallestTest(TestCase):

    def test_smallest(self):
        self.assertEqual(smallest('weather.dat'), '14')
