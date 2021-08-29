# # ============ lesson of if else statement
#
# print('WELCOME TO THE ROLLER COASTER')
# height = int(input('What is your height in CentiMeter'))
# if height >= 100:
#     print('You can rid on Roller Coaster')
# else:
#     print('Sorry! you need to grow for this rid.')

# ------------------------------------------------------------
# # Practice Program to check even and odd
# print('WELCOME TO THE EVEN AND ODD DETECTOR')
# num = int(input('Enter a Number'))
# if num % 2 == 0:
#     print('You entered an Even number!')
# else:
#     print('You entered an ODD number!')
# ------------------------------------------------------------

# ###Nested if statements
# print('WELCOME TO THE ROLLER COASTER')
# height = int(input('What is your height in CentiMeter?  '))
# age = int(input('What is your age?  '))
# if height >= 100:
#     print('You can rid on Roller Coaster')
#     if age < 12:
#         print('Pay $5')
#     elif age < 18:
#         print('Pay $7')
#     else:
#         print('Pay $12')
# else:
#     print('Sorry! you need to grow for this rid.')

# ------------------------------------------------------------
# BMI CALCULATOR
# print('WELCOME TO THE BMI CALCULATOR')
# weight = float(input('What is your Weight in Kg?  '))
# height = float(input('What is you Height in m?  '))
# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#     print('Your BMI is ' + str(bmi) + ', you are Underweight.')
# elif bmi < 25:
#     print('Your BMI is ' + str(bmi) + ', you are Normal Weight')
# elif bmi < 30:
#     print('Your BMI is ' + str(bmi) + ', you are Over Weighted')
# elif bmi < 35:
#     print('Your BMI is ' + str(bmi) + ', you are Obese')
# else:
#     print('Your BMI is ' + str(bmi) + ', you are Clinically Obese')
# # ---------------------------------------------------------------------------------
# # LEAP YEAR
# print('WELCOME TO LEAP YEAR DETECTOR')
# year = int(input('Enter Year like 1920, 2000, 2021 :  '))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f'{year} is a leap year')
#         else:
#             print(f'{year} is not a leap year')
#     else:
#         print(f'{year} is a leap year')
# else:
#     print(f'{year} is not a leap year')
# # --------------------------------------------------------------------------
# print('---------------WELCOME TO THE PIZZA ORDER PRICE CALCULATOR---------------')
# pizzaSize = input('What size of pizza do you want? S= small, M=  Medium, and L = Large  ')
# check = input('Do you want extras? (Y or N)')
# price = 0
# pizza = ''
# if pizzaSize.upper() == 'S':
#     price = 15
#     pizza = 'Small Pizza.'
# elif pizzaSize.upper() == 'M':
#     price = 20
#     pizza = 'Medium Pizza.'
# elif pizzaSize.upper() == 'L':
#     price = 25
#     pizza = 'Large Pizza'
# else:
#     print('You entered invalid input! Please Try again')
# extras = pepperoniCharge = cheeseCharge = 0
# if check.upper() == 'Y':
#     addPepperoni = input('Do you want to add pepperoni? (Y or N)')
#     if pizzaSize.upper() == 'S':
#         if addPepperoni.upper() == 'Y':
#             pepperoniCharge = 2
#             extras = extras + pepperoniCharge
#         else:
#             print('You dont want to add pepperoni on pizza')
#     else:
#         if addPepperoni.upper() == 'Y':
#             pepperoniCharge = 3
#             extras = extras + pepperoniCharge
#     addCheese = input('Do you want to add Cheese? (Y or N)')
#     if addCheese.upper() == 'Y':
#         cheeseCharge = 1
#         extras = extras + cheeseCharge
#
# print('--------Your Order-------')
# print(f'-------{pizza}-------')
# print(f'Price of Pizza              = {price}')
# print(f'Price of Extra Pepperoni    = {pepperoniCharge}')
# print(f'Price of Extra Cheese       = {cheeseCharge}')
# print(f'Your Total Bill             = {price + extras}')

# # -------------------------------------------------------------------------------
#
# yourName = input('Enter Your Name ')
# theirName = input('Enter Lover Name ')
# yourName = yourName.lower()
# theirName = theirName.lower()
#
# # true
# charCountInYN_t = yourName.count('t')
# charCountInYN_r = yourName.count('r')
# charCountInYN_u = yourName.count('u')
# charCountInYN_e = yourName.count('e')
# # love
# charCountInYN_l = yourName.count('l')
# charCountInYN_o = yourName.count('o')
# charCountInYN_v = yourName.count('v')
# charCountInYN_E = yourName.count('e')
#
# # true
# charCountIntN_t = theirName.count('t')
# charCountIntN_r = theirName.count('r')
# charCountIntN_u = theirName.count('u')
# charCountIntN_e = theirName.count('e')
# # love
# charCountIntN_l = theirName.count('l')
# charCountIntN_o = theirName.count('o')
# charCountIntN_v = theirName.count('v')
# charCountIntN_E = theirName.count('e')
# charCountInYN_True = charCountInYN_t + charCountInYN_r + charCountInYN_u + charCountInYN_e
# charCountInTN_True = charCountIntN_t + charCountIntN_r + charCountIntN_u + charCountIntN_e
# charCountInYN_Love = charCountInYN_l + charCountInYN_o + charCountInYN_v + charCountInYN_E
# charCountIntN_Love = charCountIntN_l + charCountIntN_o + charCountIntN_v + charCountIntN_E
# charCountTrue = charCountInYN_True + charCountInTN_True
# charCountLove = charCountIntN_Love + charCountInYN_Love
# love = f'{charCountTrue}{charCountLove}'
# intLove = int(love)
# if intLove < 10 or intLove > 90:
#     print(f'Your Love Score is {love}, you go together like Coke and Mentos')
# elif 40 < intLove < 50:
#     print(f'Your Love Score is {love}, you are alright together')
# else:
#     print(f'Your Love Score is {love}')
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
print('WELCOME TO THE PROJECT THREE')
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('WELCOME TO THE TREASURE ISLAND')
print('Your mission is to find out treasurer box.')
side = input( 'So where you wanna go. Type "right" or "left"')
if side == 'right':
    print('You have fall into the hole.\n GAME OVER')
elif side == 'left':
    swimWait = input('Now we are at the corner of the '
                     'lake so tell me what you want to do '
                     'wait or swim. Type "swim" or "wait"')
    if swimWait == 'swim':
        print('You have attacked by a trout.\n GAME OVER')
    elif swimWait == 'wait':
        print()
        door = input('This is your last question! Let you '
                     'tell me which color do you like in '
                     '"Red", "Blue", or Yellow')
        if door == 'yellow':
            print('CONGRATULATIONS, YOU WIN!')
        elif door == 'blue':
            print('You are eaten by Beasts. \n GAME OVER')
        elif door == 'red':
            print('You have burned by Fire. \n GAME OVER')
        else:
            print('GAME OVER')

    else:
        print('You have attacked by a trout.\n GAME OVER')

else:
    print('You have fall into the hole.\n GAME OVER')

