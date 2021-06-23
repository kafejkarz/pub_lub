import unittest
from src.pub import *

from src.customer import *

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)


    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    

    def test_till_has_cash(self):
        self.assertEqual(100.00, self.pub.till)

    # def test_pub_has_stock(self):
    #     self.assertEqual(["beer", "wine", len(self.pub)
