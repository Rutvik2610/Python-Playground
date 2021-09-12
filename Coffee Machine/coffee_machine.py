from machine_data import MENU, resources


def use_resources(menu_item, available_resources):
    req_water = MENU[menu_item]["ingredients"]["water"]
    req_milk = MENU[menu_item]["ingredients"]["milk"]
    req_coffee = MENU[menu_item]["ingredients"]["coffee"]

    avail_water = available_resources["water"]
    avail_milk = available_resources["milk"]
    avail_coffee = available_resources["coffee"]

    if (avail_water > req_water) and (avail_milk > req_milk) and (avail_coffee > req_coffee):
        avail_water -= req_water
        avail_milk -= req_milk
        avail_coffee -= req_coffee

    return resources


def use_money(quarters, dimes, nickles, pennies, menu_item):
    money_required = MENU[menu_item]["cost"]
    money_paid = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)

    if money_required > money_paid:
        print(f"Here is ${money_paid-money_required} change.")
        return money_required


def start_coffee_machine():

    money = 0
    use_coffee_machine = True
    while use_coffee_machine:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "report":
            print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")
        else:
            print("Please insert coins")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickle = int(input("How many nickles?: "))
            penny = int(input("How many pennies?: "))

            money += (quarter, dime, nickle, penny, user_input)
            resources = use_resources(user_input, resources)


start_coffee_machine()
