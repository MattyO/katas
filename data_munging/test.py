from unittest import TestCase
from smallest_temp_spread import smallest
from smallest_goal_diff import smallest_goal

class SmallestTest(TestCase):

    def test_smallest(self):
        self.assertEqual(smallest('weather.dat'), '14')

    def test_smallest_goal(self):
        self.assertEqual(smallest_goal('football.dat'), 'Aston_Villa 1')

