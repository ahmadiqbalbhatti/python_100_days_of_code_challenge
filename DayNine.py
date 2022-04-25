# # ------------------------ Dictionary In Python -----------------------
# programming_dictionary = {
#     "bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again."
# }
# #
# # # this is how can we retrieve items from dictionary
# # print(programming_dictionary["Loop"])
# # print(programming_dictionary["Function"])
# #
# # # Adding new item in dictionary
# #
# # programming_dictionary["Object"] = "Here is the definition of the Object"
# # print(programming_dictionary)
# #
# # # THis how we can remove item from dictionary
# # programming_dictionary.pop('Object')
# # print(programming_dictionary)
# #
# # # this is how we can get all values of key from dictionary
# # print(programming_dictionary.values())
# #
# # # this is how we can get all keys from dictionary
# # print(programming_dictionary.keys())
# #
# # # Get length of the dictionary
# # print(programming_dictionary.__len__())
# #
# # # Clear dictionary
# #
# # programming_dictionary.clear()
# # print(programming_dictionary)
#
# # How to loop through Dictionary
#
# for key in programming_dictionary:
#     print(key + ' = ' + programming_dictionary[key])
#     # print(programming_dictionary[key])
#
#
# # ---------------------------------------------------------
# # -------------- Grading Program --------------------------
# # ---------------------------------------------------------
#
# studentScores = {
#     'Harry': 81,
#     'Ron': 78,
#     'Hermione': 99,
#     'Draco': 74,
#     'Neville': 62,
# }
#
# studentGrades = {}
#
# for key in studentScores:
#     if studentScores[key] > 91:
#         studentGrades[key] = "Outstanding"
#     elif studentScores[key] > 81:
#         studentGrades[key] = "Exceeds Expectations"
#     elif studentScores[key] > 71:
#         studentGrades[key] = "Acceptable"
#     else:
#         studentGrades[key] = "Fail"
#
#
# for key in studentGrades:
#     print(key + " Obtains " + str(studentScores[key]) + " Marks So he Got \n" + studentGrades[key] + " Grade")

# -------------------------------------------------------------
# ----------------------- NESTING -----------------------------
# -------------------------------------------------------------

# capitals = {
#     'France': 'Paris',
#     'Germany': 'Berlin',
# }
#
# # Nesting a List in a Dictionary
# travelLog = {
#     'France': ['Paris', 'Lille'],
#     'Germany': ['Berlin', 'Hamburg', 'Stuttgart']
# }
#
# citiesList = ['Paris', 'Lille']
#
# travelLog = {
#     'France': citiesList,
#     'Germany': ['Berlin', 'Hamburg', 'Stuttgart']
# }
#
# print(travelLog)

#
# # -------------------------------------------------------------
# # ----------------------- NESTING Coding Exercise--------------
# # -------------------------------------------------------------
#
#
# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
#
#
# # 🚨 Do NOT change the code above
#
# # Write the function that will allow new countries
# # to be added to the travel_log. 👇
#
#
# # 🚨 Do not change the code below
# def add_new_country(country, visits, cities):
#     return {
#         'country': country,
#         'visits': visits,
#         'cities': cities,
#     }
#
#
# travel_log.append(add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"]))
#
# print(travel_log)

# -------------------------------------------------------------------
# ----------------------- NESTING Final Coding Exercise--------------
# -------------------------------------------------------------------
from DayNineArt import logo


def highest_bidder(bidder_list):
    high_bid_amount = 0

    for key in bidder_list:
        bid_amount = bidder_list[key]
        winner = ''
        if bid_amount > high_bid_amount:
            high_bid_amount = bid_amount
            winner = key
    print(f'The winner is {winner} with a bid of ${high_bid_amount}')


print(logo)
print('Welcome to the Secret Auction Program')

run = False

bidders = {}

while not run:
    name = input('What is your Name?:  ')
    bid = int(input("What's your bid?:    $"))
    bidders[name] = bid
    loop = input('Are there any other bidders? Type "yee" or "no".').lower()
    if loop != 'yes':
        run = True
        highest_bidder(bidders)
    else:
        run = False
