import unittest
from src.pub import *
from src.drinks import *
from src.customer import *

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Prancing Pony", 100)
        self.drinks = Drinks("beer", 5)
        self.drinks_1 = Drinks("wine", 10)
        self.drinks_2 = Drinks("cider", 5)
        self.customer = Customer("Arek", 200)
  
  
  
    
    def test_pub_has_a_name(self):
        self.assertEqual("Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_increase_till(self):
          self.pub.add_some_cash(500)
          self.assertEqual(600, self.pub.till)

   
        
    

    
      
    

    