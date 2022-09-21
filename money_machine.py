class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    def __init__(self):
        self.profit = 0
        self.amount_inserted = 0

    def process_payment(self, order_name):
        """Requests coins and calculates the total amount inserted."""
        print(f"Price is {order_name.price}$. Please insert coins.")
        for coin in self.COIN_VALUES:
            self.amount_inserted += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]

        """Checks if enough money was inserted and returns change if necessary"""
        if self.amount_inserted >= order_name.price:
            self.profit += order_name.price
            change = self.amount_inserted - order_name.price
            self.amount_inserted = 0
            if change > 0:
                print(f"Here is you change: {round(change, 2)}{self.CURRENCY}")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.profit}{self.CURRENCY}")