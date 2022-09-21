class MenuItem():
    """Models each Menu Item."""
    def __init__(self, name, price, water, milk, coffee):
        self.name = name
        self.price = price
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu():
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu_list = [
            MenuItem(name="latte", water=200, milk=200, coffee=24, price=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, price=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, price=3),
        ]
    def get_items(self):
        """Returns all the names of the available menu items"""
        menu_print = ""
        for item in self.menu_list:
            menu_print += f"{item.name}/"
        return menu_print

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu_list:
            if item.name == order_name:
                return item
        print("Sorry, this is not a valid entry")