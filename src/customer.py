class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    

    

    def add_cash(self, amount):
        self.wallet += amount

