import unittest
from src.pub import *
from src.customer import *
from src.drinks import *

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drinks = Drinks("beer", 20.00)
    
    @unittest.skip("Delete this line to run the test")
    def test_drink_has_name(self):
        self.assertEqual("beer", self.drinks.name) 
    
    @unittest.skip("Delete this line to run the test")
    def test_drink_has_price(self):
        self.assertEqual(20.00, self.drinks.price) 
        

    