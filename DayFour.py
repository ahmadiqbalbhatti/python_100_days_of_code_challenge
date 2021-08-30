# random_int = random.randint(0, 6)
# print(random_int)
#
# random_float = random.uniform(0, 5)
# random_float  * 5
# print(random_float)
# # ----------------------------------------- FIRST CODING EXERCISE------------------------------------------
# print("Welcome to Heads & Tail Generator:\n")
# randomNum = random.randint(0, 1)
# if randomNum == 0:
#     print('Tails')
# else:
#     print('Heads')

# # -----------------------DATA STRUCTURE (LIST)
# statesOfPakistan = ["Sindh", "Punjab", "Khyber Pakhtunekhwa", "Islamabad Capital Territory", "Gilgit-Baltistan",
#                     "Baluchistan", "Azad Jammu and Kashmir"]
# statesOfPakistan.append("Azad Jammu and Kashmir")
# statesOfPakistan.pop(6)
# statesOfPakistan.insert(0, '34')
# statesOfPakistan.reverse()
# statesOfPakistan.sort()

# copyOfStates = statesOfPakistan.copy()
# print(copyOfStates)
# statesOfPakistan.clear()
# print(statesOfPakistan)
# print(copyOfStates.pop())
# print(copyOfStates)
# # ----------------------------------------- SECOND CODING EXERCISE ---------------------------------------
# print('WELCOME TO THE NAME SELECTOR FOR PAYING BILL')
# print('Give me Names of Everybody, Separated by comma and space like (, )')
# nameString = input()
# names = nameString.split(", ")
# length = names.__len__()
# length = length-1
# randomListNameSelector = random.randint(0, length)
# print(f'{names[randomListNameSelector]} should pay the bill!')
# # -----------------------------DATA STRUCTURE (Nested LIST)
# statesOfPakistan = ["Sindh", "Punjab", "Khyber Pakhtunekhwa", "Islamabad Capital Territory",
#                     "Gilgit-Baltistan", "Baluchistan", "Azad Jammu and Kashmir"]
# numOfStates = len(statesOfPakistan)
# print(statesOfPakistan[numOfStates-1])

# dirtyDozen = ["Strawberries", "Spinach", "Apples", "Grapes", "Tomatoes", "Potatoes"]

# fruits = ["Strawberries", "Apples", "Grapes"]
# vegetables = ["Spinach", "Tomatoes", "Potatoes"]
# dirtyDozen = [fruits, vegetables]
# print(fruits)
# print(vegetables)
# print(dirtyDozen)
# # # ----------------------------------------- THIRD CODING EXERCISE ---------------------------------------
# print('welcome to the program which will mark a spot with an \'X\''.upper())
# row1 = ["😆", "😂", "😚"]
# row2 = ["😆", "😂", "😚"]
# row3 = ["😆", "😂", "😚"]
# print(f'    1     2     3 \n1 {row1}\n2 {row2}\n3 {row3}')
# map = [row1, row2, row3]
# print(map)
# address = input('Where you want to place \"X\"')
# column = int(address[0])  # 2
# row = int(address[1])  # 3
# # print(column {column} and row is {row}')
# map[row-1][column-1]= "X"
# # print(map[column-1])
# # ==========Simple Method
# # selectedRow = map[row - 1]
# # selectedRow[column-1] = "X"
#
# # ==========Easy and Long Method
# # if address == 11:
# #     row1[0] = "X"
# # elif address == 12:
# #     row1[1] = "X"
# # elif address == 13:
# #     row1[2] = "X"
# # elif address == 21:
# #     row2[0] = "X"
# # elif address == 22:
# #     row2[1] = "X"
# # elif address == 23:
# #     row2[2] = "X"
# # elif address == 31:
# #     row3[0] = "X"
# # elif address == 32:
# #     row3[1] = "X"
# # elif address == 33:
# #     row3[2] = "X"
# print(f'    1     2     3 \n1 {row1}\n2 {row2}\n3 {row3}')
# ---------------------------------------------Day Four Project---------------------------
import random

print("WELCOME TO THE ROCK PAPER SCISSORS GAME")
print('''What do you choose?
      Type "0" for Rock,
      Type "1" for Paper,
      Type "2" for Scissors''')
userInput = input()
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
if userInput == "0":
    print('You choose Rock.')
    print(rock)
elif userInput == "1":
    print('You choose Paper.')
    print(paper)
elif userInput == "2":
    print('You choose Scissors.')
    print(scissors)
else:
    print('YOU ENTERED AN INVALID NUMBER')
    exit()
computerChoose = str(random.randint(0, 2))
if computerChoose == "0":
    print('Computer choose Rock.')
    print(rock)
elif computerChoose == "1":
    print('Computer choose Paper.')
    print(paper)
elif computerChoose == "2":
    print('Computer choose Scissors.')
    print(scissors)
print('RESULT')
if userInput == "0" and computerChoose == "2":
    print('You WIN!')
elif userInput == "1" and computerChoose == "0":
    print('You WIN!')
elif userInput == "2" and computerChoose == "1":
    print('You WIN!')  # ends user wins
elif userInput == "2" and computerChoose == "0":
    print('COMPUTER WIN!')
elif userInput == "0" and computerChoose == "1":
    print('COMPUTER WIN!')
elif userInput == "1" and computerChoose == "2":
    print('COMPUTER WIN!')
elif userInput == computerChoose:
    print('DRAW')
