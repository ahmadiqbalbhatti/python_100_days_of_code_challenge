# ==================   Second Way of Making BlackJack  =====================

# list of Cards [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
import random
from replit import clear

from DayElevenProject import logo

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    # How to add Funcation definition for Hover
    """This function will return cards from the Deck."""
    # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(card):
    """Calculate Score function will take a List of Cards and Return the Score Calculated from the card list"""
    # if 11 in cards and 10 in cards and len(cards) == 2:
    # or
    if sum(card) == 21 and len(card) == 2:
        return 0

    if 11 in cards and sum(card) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(card)


def compare(user_scores, computer_scores):
    if user_scores == computer_scores:
        return "Draw"
    elif computer_scores == 0:
        return "Lose, Opponent has Blackjack!"
    elif user_scores == 0:
        return "Win with a Blackjack"
    elif user_scores > 21:
        return "You went Over, Lose!"
    elif computer_scores > 21:
        return "You Win, Opponent went over"
    elif user_scores > computer_scores:
        return "You WIN"
    else:
        return "You LOSE"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your Cards:  {user_cards} & Your Current Score: {user_score}")
        print(f"Computer Cards:  {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your Final Cards: {user_cards}, Your Final Score: {user_score}")
    print(f"    Computer's Final Cards: {computer_cards}, Computer's Final Score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Want to Restart Game\nPass 'y' for play and 'n' for exit").lower() == "y":
    clear()
    play_game()
