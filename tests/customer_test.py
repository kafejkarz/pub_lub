import unittest
from src.pub import *
from src.customer import *

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Juan", 100.00)

    def test_customer_has_name(self):
        self.assertEqual("Juan", self.customer.name)

    def test_customer_has_cash(self):
        self.assertEqual(100.00, self.customer.wallet)