class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    

    def can_customer_buy_drink(self, wallet):
        if self.wallet >= 20.00:
            return True

