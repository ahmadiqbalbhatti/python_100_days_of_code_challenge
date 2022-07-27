# # List Comprehensions
# # Example Task1
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# # Write your 1 line code 👇 below:
#
# squared_numbers = [number * number for number in numbers]
#
# # Write your code 👆 above:
#
# print(f'List of Squared Numbers = {squared_numbers}')
#
# # ----------------------------------------------------------
#
# # Example Task 2
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# # Write your 1 line code 👇 below:
#
# result = [number for number in numbers if number % 2 == 0]
#
# # Write your code 👆 above:
#
# print(f'List of Even Numbers = {result}')
#
# # ----------------------------------------------------------
#
# # Example Task 3
#
# with open("file1.txt") as file1:
#     list_one = file1.readlines()
#
# with open("file2.txt") as file2:
#     list_two = file2.readlines()
#
# result = [int(number) for number in list_one if number in list_two]
# print(list_one)
# print(list_two)
#
#
# # Write your code above 👆
#
# print(result)
#

# DICTIONARY COMPREHENSION
import random

names = ['alex', 'beth', 'caroline', 'dave', 'eleanor', 'freddie']
# print(names)
#
# students_score = {student: random.randint(0, 101) for student in names}
# print(students_score)
#
# passed_student = {student: score for (student, score) in students_score.items() if score >= 60}
#
# print(passed_student)


# ------------------------------------------------------
# # Exercise Task 4
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow ?"
# # Don't change code above 👆
#
# list_words = sentence.split()
#
# result = {word: len(word) for word in list_words}
#
# # Write your code below:
#
#
# print(result)


# ------------------------------------------------------
# # Exercise Task 5
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
# weather_f = {day: (temp * (9 / 5) + 32).__format__(".2f") for (day, temp) in weather_c.items()}
#
# # Write your code 👇 below:
#
# print(weather_f)
