from VCM_Data import MENU, resources

res_water = resources['water']
res_milk = resources['milk']
res_coffee = resources['coffee']

print(f"water : {res_water}, milk: {res_milk}, coffee: {res_coffee}")


def print_resources():
    print("=================================================")
    print("Current Resources")
    print("=================================================")
    print(f"Water:{res_water}ml")
    print(f"Milk: {res_milk}ml")
    print(f"Coffee: {res_coffee}g")
    print("=================================================")


def check_resources(coffee, res_water, res_milk, res_coffee):
    # # print(f"Water In Resources: {resources['water']} and Water in Menu: {MENU[coffee]['ingredients']['water']}")
    # print(f"{resources['water'] - MENU[coffee]['ingredients']['water']}")
    # print(f"{resources['milk'] - MENU[coffee]['ingredients']['milk']}")
    # print(f"{resources['coffee'] - MENU[coffee]['ingredients']['coffee']}")
    if res_water > MENU[coffee]['ingredients']['water'] and res_milk > MENU[coffee]['ingredients'][
        'milk'] and res_coffee > MENU[coffee]['ingredients']['coffee']:
        res_water -= MENU[coffee]['ingredients']['water']
        res_milk -= MENU[coffee]['ingredients']['milk']
        res_coffee -= MENU[coffee]['ingredients']['coffee']
        return 1
    else:
        return 0


def process_coins():
    # quarters =  $0.25
    # dimes =  $0.10
    # nickles =  $0.05
    # pennies =  $0.01
    quarters = int(input('How many Quarters? : '))
    dimes = int(input('How many Dimes? : '))
    nickles = int(input('How many Nickles? : '))
    pennies = int(input('How many Pennies? : '))
    coins = (quarters * 0.25) + (nickles * 0.05) + (dimes * 0.10) + (pennies * 0.01)
    return coins


def is_transaction_successful(coins, coffee):
    if coins >= MENU[coffee]['cost']:
        return True
    if coins > MENU[coffee]['cost']:
        print(f"Get your balance Coins {coins - MENU[coffee]['cost']}")
    if coins < MENU[coffee]['cost']:
        return False


def balance_coin(coins, coffee):
    if coins > MENU[coffee]['cost']:
        print("_____________________________________")
        print("Get your Balance")
        print("-------------------------------------")
        bal_coin = coins - MENU[coffee]['cost']
        if bal_coin > 0.25:
            quarter = bal_coin / 0.25
            bal_coin = bal_coin % 0.25
            print(f"{round(quarter)} Quarters")
        if bal_coin > 0.10:
            dimes = bal_coin / 0.10
            bal_coin = bal_coin % 0.10
            print(f"{round(dimes)} Dimes")
        if bal_coin > 0.05:
            nickles = bal_coin / 0.05
            bal_coin = bal_coin % 0.05
            print(f"{round(nickles)} Nickles")
        if bal_coin >= 0.01:
            pennies = bal_coin / 0.01
            # bal_coin = bal_coin % 0.01
            print(f"{round(pennies)} Pennies")

        # print(f"Get your balance Coins {coins - MENU[coffee]['cost']}")


def get_coffee(coffee):
    coin = process_coins()
    print(f"You Entered : ${round(coin, 2)}")
    is_transaction = is_transaction_successful(coin, coffee)
    if is_transaction:
        print(f"Get your {coffee}, Enjoy!")
    else:
        print(f"Please Enter Correct Amount of Coins")
        print(f"Take your Coins")
    balance_coin(coin, coffee)


flag = False
while not flag:
    user_input = input('What would you Like? (espresso/latte/cappuccino)').lower()
    if user_input == 'espresso':
        print('Inset the Cones in Machine for Espresso : $', MENU['espresso']['cost'])
        get_coffee('espresso')
    elif user_input == 'latte':
        print('Inset the Cones in Machine for Latte : $', MENU['latte']['cost'])
        get_coffee('latte')
    elif user_input == 'cappuccino':
        print('Inset the Cones in Machine for cappuccino : $', MENU['cappuccino']['cost'])
        get_coffee('cappuccino')
    elif user_input == 'report':
        print_resources()
    elif user_input == 'off':
        exit()
    else:
        print('Invalid Input')
