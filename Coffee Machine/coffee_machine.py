from machine_data import MENU, resources


def check_resources(order_requirements):
    """Checks if the available resources are sufficient for the ordered item"""
    for item in order_requirements:
        if order_requirements[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def use_resources(order_requirements, available_resources):
    """Deducts the ingredients used for the order and returns the available resources."""
    for item in order_requirements:
        available_resources[item] -= order_requirements[item]
    return available_resources


def use_money(quarters, dimes, nickles, pennies, menu_item):
    """Checks if the money paid is sufficient. If it is then gives user back the change if any.
     if it is not then refunds all the money"""
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
    elif user_input == "off":
        use_coffee_machine = False
    else:
        if check_resources(MENU[user_input]["ingredients"]):
            print("Please insert coins")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickle = int(input("How many nickles?: "))
            penny = int(input("How many pennies?: "))

            money = use_money(quarter, dime, nickle, penny, user_input)
            if money != 0:
                money_in_machine += money
                resources = use_resources(MENU[user_input]["ingredients"], resources)
                print(f"Here is your {user_input}. Enjoy!")
