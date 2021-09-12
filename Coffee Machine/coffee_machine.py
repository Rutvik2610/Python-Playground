from machine_data import MENU, resources
import math


def use_resources(menu_item, available_resources):
    req_water = MENU[menu_item]["ingredients"]["water"]
    req_milk = MENU[menu_item]["ingredients"]["milk"]
    req_coffee = MENU[menu_item]["ingredients"]["coffee"]

    avail_water = available_resources["water"]
    avail_milk = available_resources["milk"]
    avail_coffee = available_resources["coffee"]

    if avail_water > req_water:
        if avail_milk > req_milk:
            if avail_coffee > req_coffee:
                available_resources["water"] -= req_water
                available_resources["milk"] -= req_milk
                available_resources["coffee"] -= req_coffee
                print(f"Here is your {menu_item}. Enjoy!")
            else:
                print("Sorry there is not enough Coffee")
        else:
            print("Sorry there is not enough Milk")
    else:
        print("Sorry there is not enough Water")

    return resources


def use_money(quarters, dimes, nickles, pennies, menu_item):
    money_required = MENU[menu_item]["cost"]
    money_paid = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    if money_required < money_paid:
        total_change = round((money_paid - money_required), 2)
        print(f"Here is ${money_paid - money_required} change.")
        return money_required
    else:
        print("Sorry that's not enough money. Money refunded")
        return 0


money = 0
use_coffee_machine = True
while use_coffee_machine:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${money}")
    elif user_input == "exit":
        use_coffee_machine = False
    else:
        print("Please insert coins")
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickle = int(input("How many nickles?: "))
        penny = int(input("How many pennies?: "))

        money += use_money(quarter, dime, nickle, penny, user_input)
        resources = use_resources(user_input, resources)
