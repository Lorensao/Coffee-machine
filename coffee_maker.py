class CoffeeMaker:
    def __init__(self):
        """Models the machine that makes the coffee"""
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml\nMilk: {self.resources['milk']}ml\nCoffee: {self.resources['coffee']}g")

    def is_resources_sufficient(self, order_name):
        """Returns True when order can be made, False if ingredients are insufficient."""
        sufficient = True
        for item in order_name.ingredients:
            if order_name.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                sufficient = False
        return sufficient

    def make_coffee(self, order_name):
        """Deducts the required ingredients from the resources."""
        for item in self.resources:
            self.resources[item] -= order_name.ingredients[item]
        # or
        # self.resources["water"] -= order_name.ingredients["water"]
        # self.resources["milk"] -= order_name.ingredients["milk"]
        # self.resources["coffee"] -= order_name.ingredients["coffee"]
        print(f"Here is your {order_name.name}. Enjoy!")