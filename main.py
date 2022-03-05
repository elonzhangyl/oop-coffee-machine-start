from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


# menu_item = MenuItem()
menu = Menu()

# money_machine.make_payment(cost)
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}:")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

    # if choice == "off":
    #     break
    #
    # if choice == "report"
    #     CoffeeMaker.report()
    #
    # if choice == "espresso" or "latte" or "cappuccino":
    #     CoffeeMaker.is_resource_sufficient()