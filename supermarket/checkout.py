from collections import namedtuple

Item = namedtuple(sku, price, special)
Special = namedtuple(number_of, for_price)

RuleApplication(item_index, rule_name, old_price, new_price)
GroupReduction(skus, new_price)

def parse_special(some_text):
    return Special(0, 0.0)

class SuperMarket():
    def __init__(self):
        self.items = []
        self.cart = []

    def add_item(self, sku, price, special_price):
        return items.append(Item(sku, float(price), parse_special(special_price))

    def scan(self, sku):
       self.cart.append(self._find_item(sku))

    def _find_item(self, sku):
        return next(filter(lambda i: i.sku == sku, self.items), None)

    @property
    def total(self):
        
        return sum( [self._find_item(sku).price for item in items] )
