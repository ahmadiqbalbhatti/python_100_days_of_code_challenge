from VCM_Data import MENU

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """This function Returns True When order can be made"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, There is not enough {item}")
            is_enough = False
    return is_enough


def process_coins():
    """This function returns the total calculated from the given coins """
    print("Please Insert Coins.")
    total = int(input("How many Quarters?")) * 0.25
    total += int(input("How many Dimes?")) * 0.1
    total += int(input("How many Nickles?")) * 0.05
    total += int(input("How many Pennies?")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """This function will Return True when payment is accepted or vice versa"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry! That's not enough to Buy. Money Refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """This function will deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):  ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
