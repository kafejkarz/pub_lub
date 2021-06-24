import unittest
from src.pub import *
from src.customer import *
from src.drinks import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Arek", 200)
        

    
    # po def okresl co chcesz przetestowac
    # nastepnie przez self wskaz czego/kogo ma to dotyczyc 
    # stworz nazwe metody(oraz podaj argument)
    # self.assertEqual(przewidywany outcome, sciezka docelowa)


    
    def test_add_some_cash_to_arek_wallet(self):
         self.customer.add_cash(100)
         self.assertEqual(300, self.customer.wallet)
    


    