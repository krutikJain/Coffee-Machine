from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
menu = Menu()
coin = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    order = input(f"What would you like to order {options}")
    if order == "off":
        is_on = False
    elif order == "report":
        coffee.report()
        coin.report()
    else:
        drink = menu.find_drink(order)
        if coffee.is_resource_sufficient(drink) and coin.make_payment(drink.cost):
            coffee.make_coffee(drink)
