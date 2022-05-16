import random

from DayElevenProject import logo

print(logo)
# ==================   One Way of Making BlackJack  =====================
# Its hard to understand
# it is a rough code
# it is not tackling every point from the list

# list of Cards [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []


def random_cards():
    my_random_index = random.randint(1, 11)
    return cards[my_random_index]


print(random_cards())

for i in range(2):
    your_cards.append(random_cards())

print("Your Cards: ", your_cards)

for i in range(1):
    computer_cards.append(random_cards())

print("Computer's First Cards: ", computer_cards)

loop = False

while not loop:
    check = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if check.__eq__("n"):
        # computer_cards.append(random_cards())
        print("Your Final Cards at Hand: ", your_cards)
        # print("Computer's Final Cards: ", computer_cards)
        your_cards_sum = 0
        computer_cards_sum = 0
        for j in your_cards:
            your_cards_sum += j
        for k in computer_cards:
            computer_cards_sum += k

        # turn comment off to test what it is
        # print(your_cards_sum)
        # print(computer_cards_sum)
        if your_cards_sum > 21:
            print("Computer's Final Cards: ", computer_cards)
            print("You Lose!")
        elif computer_cards_sum > 21:
            print("You Won!")
        elif your_cards_sum <= 21 and computer_cards_sum <= 21:
            computer_cards.append(random_cards())
            print("Computer's Final Cards: ", computer_cards)
            computer_cards_sum = 0
            for k in computer_cards:
                computer_cards_sum += k
            print("Computerr card sum ", computer_cards_sum)
            if your_cards_sum > computer_cards_sum:
                # if computer_cards_sum <= 21:
                # print("Computer's Final Cards: ", computer_cards)
                print("Computer LOSE")
                print("YOU WON!")
            elif your_cards_sum < computer_cards_sum:
                print("Computer WON")
                print("You LOSE!")
            elif your_cards_sum == computer_cards_sum:
                print("Game DRAW")

        # if computer_cards_sum < 22 & your_cards_sum
        #     if computer_cards_sum < your_cards_sum:
        #         computer_cards.append(random_cards())
        #         print("Computer's Final Cards: ", computer_cards)
        #
        #     elif computer_cards_sum == your_cards_sum:
        #         print("DRAW")
        #     elif computer_cards_sum > your_cards_sum:
        #         print("Computer Wins")

        loop = True
    elif check.__eq__("y"):
        your_cards.append(random_cards())
        computer_cards.append(random_cards())
        print("Your Cards: ", your_cards)
        print("Computer's Final Cards: ", computer_cards)
        # your_cards_sum = 0
        # computer_cards_sum = 0
        # for j in your_cards:
        #     your_cards_sum += j
        # for k in computer_cards:
        #     computer_cards_sum += k
        loop = False
    else:
        print()

