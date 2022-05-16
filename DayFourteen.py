import random

from DayFourteenArtGameData import data, logo, vs

print(logo)


def compare_accounts(account1, account2):
    if int(account1['follower_count']) > int(account2['follower_count']):
        return 1
    elif int(account2['follower_count']) > int(account1['follower_count']):
        return 2
    elif int(account1['follower_count']) == int(account2['follower_count']):
        return 3


def counter(score_count):
    if score_count == 0:
        print("Current Score: ", str(score_count))
    else:
        print("===========================================================================")
        print(f"================= You are Right! Your Current Score: {score_count} ====================")
        print("===========================================================================")


count = 0
flag = True
while flag:
    account_one = random.choice(data)
    print(f"Compare Account 01: {account_one['name']}, {account_one['description']}, {account_one['country']}")
    print(vs)
    account_two = random.choice(data)
    print(f"Against Account 02: {account_two['name']}, {account_two['description']}, {account_two['country']}")
    user_input = int(input("Who has more followers? Type '1' or '2' :      "))
    if user_input == 1:
        if user_input == compare_accounts(account_one, account_two):
            count += 1
            counter(count)
            # flag = True
        else:
            flag = False
            print("***************************************************************************")
            print(f"You Lose! With Score: {count}")
            print("***************************************************************************")
    elif user_input == 2:
        if user_input == compare_accounts(account_one, account_two):
            count += 1
            counter(count)
            # flag = True
        else:
            flag = False
            print("***************************************************************************")
            print(f"You Lose! With Score: {count}")
            print("***************************************************************************")
    else:
        break






