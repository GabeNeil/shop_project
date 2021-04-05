import unittest

from models.manufacturer import Manufacturer

class ManufacturerTest(unittest.TestCase):
    
    def setUp(self):
        self.manufacturer = Manufacturer("Fender")

    def test_name(self):
        self.assertEqual("Fender", self.manufacturer.name)