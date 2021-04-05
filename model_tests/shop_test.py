import unittest

from models.shop import Shop 

class ShopTest(unittest.TestCase):

    def setUp(self):
        self.shop = Shop("Gabe's Gabetars", 3000)

    def test_shop_has_name(self):
        self.assertEqual("Gabe's Gabetars", self.shop.name)

    def test_shop_has_till(self):
        self.assertEqual(3000, self.shop.till)