from menu import MenuItem, Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on == True:
    selection = input(f"What would you like? {menu.get_items()}: " )
    if selection == "off":
        machine_on = False
    elif selection == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        selection = menu.find_drink(selection)
        if coffee_maker.is_resources_sufficient(selection) == True:
            if money_machine.process_payment(selection) == True:
                coffee_maker.make_coffee(selection)














