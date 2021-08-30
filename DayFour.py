import math
import random

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
# statesOfPakistan = ["Sindh", "Punjab", "Khyber Pakhtunekhwa", "Islamabad Capital Territory", "Gilgit-Baltistan",
#                     "Baluchistan", "Azad Jammu and Kashmir"]
# numOfStates = len(statesOfPakistan)
# print(statesOfPakistan[numOfStates-1])

# dirtyDozen = ["Strawberries", "Spinach", "Apples", "Grapes", "Tomatoes", "Potatoes"]

# fruits = ["Strawberries", "Apples", "Grapes"]
# vegetables = ["Spinach", "Tomatoes", "Potatoes"]
# dirtyDozen = [fruits, vegetables]
# print(fruits)
# print(vegetables)
# print(dirtyDozen)
# # ----------------------------------------- THIRD CODING EXERCISE ---------------------------------------
print('welcome to the program which will mark a spot with an \'X\''.upper())
row1 = ["😆", "😂", "😚"]
row2 = ["😆", "😂", "😚"]
row3 = ["😆", "😂", "😚"]
print(f'    1     2     3 \n1 {row1}\n2 {row2}\n3 {row3}')
map = [row1, row2, row3]
print(map)
address = input('Where you want to place \"X\"')
column = int(address[0])  # 2
row = int(address[1])  # 3
print(f'column {column} and row is {row}')
# print(map[column-1])
selectedRow = map[row - 1]
selectedRow[column-1] = "X"

# if address == 11:
#     row1[0] = "X"
# elif address == 12:
#     row1[1] = "X"
# elif address == 13:
#     row1[2] = "X"
# elif address == 21:
#     row2[0] = "X"
# elif address == 22:
#     row2[1] = "X"
# elif address == 23:
#     row2[2] = "X"
# elif address == 31:
#     row3[0] = "X"
# elif address == 32:
#     row3[1] = "X"
# elif address == 33:
#     row3[2] = "X"
print(f'    1     2     3 \n1 {row1}\n2 {row2}\n3 {row3}')
