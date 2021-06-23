import unittest
from src.pub import *
from src.drinks import *
from src.customer import *

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    @unittest.skip("Delete this line to run the test")
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    @unittest.skip("Delete this line to run the test")
    def test_till_has_cash(self):
        self.assertEqual(100.00, self.pub.till)

    @unittest.skip("Delete this line to run the test")
    def test_can_sell_drink_to_customer(self):
        self.assertEqual(True, self.customer.wallet)
        self.assertEqual(80.00, self.subtract.wallet(20.00))
        self.assertEqual(120.00, self.pub.till)
      
    

    