import unittest
from src.pub import *
from src.customer import *
from src.drinks import *

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drinks = Drinks("beer", 5)
        self.drinks_1 = Drinks("wine", 10)
        self.drinks_2 = Drinks("cider", 5)
    
    
    
    def test_pub_has_a_drinks(self):
        self.assertEqual("cider", self.drinks_2.name)