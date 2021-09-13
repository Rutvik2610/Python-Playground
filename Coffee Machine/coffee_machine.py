from machine_data import MENU, resources


def check_resources(menu_item, available_resources):
    req_water = MENU[menu_item]["ingredients"]["water"]
    req_coffee = MENU[menu_item]["ingredients"]["coffee"]

    avail_water = available_resources["water"]
    avail_coffee = available_resources["coffee"]

    if avail_water > req_water:
        if avail_coffee > req_coffee:
            if menu_item != "espresso":
                req_milk = MENU[menu_item]["ingredients"]["milk"]
                avail_milk = available_resources["milk"]
                if avail_milk > req_milk:
                    return True
                else:
                    print("Sorry there is not enough Milk")
            else:
                return True
        else:
            print("Sorry there is not enough Coffee")
            return False
    else:
        print("Sorry there is not enough Water")
        return False


def use_resources(menu_item, available_resources):
    req_water = MENU[menu_item]["ingredients"]["water"]
    req_coffee = MENU[menu_item]["ingredients"]["coffee"]

    available_resources["water"] -= req_water
    available_resources["coffee"] -= req_coffee

    if menu_item != "espresso":
        req_milk = MENU[menu_item]["ingredients"]["milk"]
        available_resources["milk"] -= req_milk

    print(f"Here is your {menu_item}. Enjoy!")

    return available_resources


def use_money(quarters, dimes, nickles, pennies, menu_item):
    money_required = MENU[menu_item]["cost"]
    money_paid = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    if money_required < money_paid:
        total_change = round((money_paid - money_required), 2)
        print(f"Here is ${total_change} change.")
        return money_required
    else:
        print("Sorry that's not enough money. Money refunded")
        return 0


money_in_machine = 0
money = money_in_machine
use_coffee_machine = True
while use_coffee_machine:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\n"
              f"Money: ${money_in_machine}")
    elif user_input == "exit":
        use_coffee_machine = False
    else:
        if check_resources(user_input, resources):
            print("Please insert coins")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickle = int(input("How many nickles?: "))
            penny = int(input("How many pennies?: "))

            money = use_money(quarter, dime, nickle, penny, user_input)
            if money_in_machine != money:
                money_in_machine += money
                resources = use_resources(user_input, resources)
