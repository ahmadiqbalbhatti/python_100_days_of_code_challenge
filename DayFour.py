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

# -----------------------DATA STRUCTURE (LIST)
statesOfPakistan = ["Sindh", "Punjab", "Khybr Pakhtunekhwa", "Islamabad Capital Territory", "Gilgit-Baltistan",
                    "Baluchistan", "Azad Jammu and Kashmir"]
# statesOfPakistan.append("Azad Jammu and Kashmir")
# statesOfPakistan.pop(6)
# statesOfPakistan.insert(0, '34')
# statesOfPakistan.reverse()
# statesOfPakistan.sort()

copyOfStates = statesOfPakistan.copy()
print(copyOfStates)
statesOfPakistan.clear()
print(statesOfPakistan)
print(copyOfStates.pop())
print(copyOfStates)

