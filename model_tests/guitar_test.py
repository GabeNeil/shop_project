import unittest

from models.guitar import Guitar 

class GuitarTest(unittest.TestCase):

    def setUp(self):
        self.guitar = Guitar("Stratocaster", "classic design", 5, 300, 600, "Fender")

    def test_guitar_name(self):
        self.assertEqual("Stratocaster", self.guitar.name)

    def test_guitar_description(self):
        self.assertEqual("classic design", self.guitar.description)

    def test_guitar_buy_cost(self):
        self.assertEqual(300, self.guitar.buy_cost)

    def test_guitar_sell_price(self):
        self.assertEqual(600, self.guitar.sell_price)

    def test_manufacturer_name(self):
        self.assertEqual("Fender", self.guitar.manufacturer)