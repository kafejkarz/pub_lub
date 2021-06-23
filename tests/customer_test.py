import unittest
from src.pub import *
from src.customer import *
from src.drinks import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Juan", 100.00)

    
    
    @unittest.skip("Delete this line to run the test")
    def test_customer_has_name(self):
        self.assertEqual("Juan", self.customer.name)
    
    @unittest.skip("Delete this line to run the test")
    def test_customer_has_cash(self):
        self.assertEqual(100.00, self.customer.wallet)

    def test_customer_buys_drink(self):
        self.assertEqual(True, self.customer.wallet)