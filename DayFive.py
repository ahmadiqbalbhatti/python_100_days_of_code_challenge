# fruit = ["Apple", "Peach", "Pear"]
# for fruits in fruit:
#     print(fruits)
# -----------------------------------------------First Exercise of Day 5-----------------------
# print('Welcome to the Student Height average calculator'.upper())
# studentHeight = input('Insert a list of Height of Students in centimeters: ').split()
# numberOfStudents = 0
# for n in range(0, len(studentHeight)):
#     studentHeight[n] = int(studentHeight[n])
#     numberOfStudents += 1
# # print(studentHeight)
# print(f'Number of the Students = {numberOfStudents}')
# totalHeight = 0
# for studentHeights in studentHeight:
#     totalHeight += studentHeights
# # averageHeight = sum(studentHeight) / len(studentHeight)
# averageHeight = totalHeight / numberOfStudents
# print(f'Average Student Height is {round(averageHeight)}cm')
# # -----------------------------------------------Second Exercise of Day 5-----------------------
# print('Welcome to the Student Highest and Lowest Score Finder'.upper())
# studentScores = input('Input list of Student Scores : ').split()
# for n in range(0, len(studentScores)):
#     studentScores[n] = int(studentScores[n])
# print(studentScores)
# # myMax = max(studentScores)
# # myMin = min(studentScores)
# myMax = studentScores[0]
# myMin = studentScores[0]
# for studentScore in studentScores:
#     if studentScore > myMax:
#         myMax = studentScore
#     if studentScore < myMin:
#         myMin = studentScore
# print(f'The highest score in the class is {myMax}')
# print(f'The lowest score in the class is {myMin}')
# ----------------------------------------------- This is how we can use range key word-----------
# num = 101
# mySum = 0
# for n in range(1, num):
#     # print(n)
#     mySum += n
# print(mySum)
# #print(1001 * 500)
#  # # -----------------------------------------------Third Exercise of Day 5-----------------------
# print('LETS CALCULATE THE EVEN NUMBERS')
# inputNumber = int(input('Input a Number till you want to calculate even Number: '))
# mySum = 0
# # Method #1
# # for num in range(1, inputNumber+1):
# #     if num % 2 == 0:
# #         mySum += num
# # Method #2
# for num in range(2, inputNumber + 1, 2):
#     mySum += num
# print(f'Sum of all Even Numbers Between 1 to {inputNumber} is {mySum}')
# #  # # -----------------------------------------------Fourth Exercise of Day 5-----------------------
# print('Welcome to the Fizz Buzz FizzBuzz Game')
# for num in range(1, 101):
#     if num % 3 == 0:
#         print('FIZZ')
#     elif num % 5 == 0:
#         print('BUZZ')
#     elif num % 3 == 0 and num % 5 == 0:
#         print('FIZZBUZZ')
#     else:
#         print(num)
# ---------------------------------------------------Final Project of the Day 5------------------------------
import random
print('WELCOME TO THE PyPASSWORD GENERATOR')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

inputLetters = int(input("How many letters would you like in your password?\n"))
inputSymbols = int(input(f"How many symbols would you like?\n"))
inputNumbers = int(input(f"How many numbers would you like?\n"))
