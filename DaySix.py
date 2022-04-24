# ----------Day 6 is about to Discuss Functions and While Loop ---------
# # How to define a Function
# def my_function(a):
#     print(f'{a}th Times Printed')
#     print('Hello world!')
#     print('We are here to help you in the digital world')
#
#
# my_function(1)
# my_function(2)
# my_function(3)
# my_function(4)

# How to define a loop
# ---- Let see how can I print a table
# num = int(input('Enter a Number'))
# condition = 1
# while condition <= 10:
#     print(f'{num} * {condition} = {num * condition}')
#     condition += 1

# Let create a Parameterized Function
def table(number):
    condition = 1
    while condition <= 10:
        print(f'{number} * {condition} = {number * condition}')
        condition += 1


num = int(input('Enter a Number'))
table(num)
