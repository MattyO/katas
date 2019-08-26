import checkout
from unittest import TestCase

class SuperMarketTest(TestCase):

    def setUp(self):
        self.super_market = checkout.SuperMarket()

    def test_checkout_single_item(self):
        self.super_market.add_item("A", 50, '3 for 120')
        self.super_market.scan("A")
        self.assertEqual(self.super_market.total, 50)

    def test_checkout_two_different_items(self):
        self.super_market.add_item("A", 50, '3 for 120')
        self.super_market.add_item("B", 30, '2 for 45')
        self.super_market.scan("A")
        self.super_market.scan("B")
        self.assertEqual(self.super_market.total, 80)

    def test_checkout_for_1_special_set(self):
        self.super_market.add_item("A", 50, '3 for 120')
        self.super_market.scan("A")
        self.super_market.scan("A")
        self.super_market.scan("A")
        self.assertEqual(self.super_market.total, 120)

    def test_checkout_for_1_special_but_some_extra(self):
        self.super_market.add_item("A", 50, '3 for 120')
        [ self.super_market.scan("A") for i in range(0,5) ]
        self.assertEqual(self.super_market.total, 120 + (50 * 2))

    def test_checkout_special_set_with_another_sku_in_between(self):
        self.super_market.scan("A")
        self.super_market.scan("A")
        self.super_market.scan("B")
        self.super_market.scan("A")

        self.assertEqual(self.super_market.total, 120 + 30)

