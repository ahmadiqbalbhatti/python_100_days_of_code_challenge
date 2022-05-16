# python has no block scope
import random

logo = '''███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗      ██████╗ ██╗   ██╗███████╗███████╗███████╗██╗███╗   ██╗ ██████╗      ██████╗  █████╗ ███╗   ███╗███████╗
████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝██║████╗  ██║██╔════╝     ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝    ██║  ███╗██║   ██║█████╗  ███████╗███████╗██║██╔██╗ ██║██║  ███╗    ██║  ███╗███████║██╔████╔██║█████╗  
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║██║██║╚██╗██║██║   ██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ╚██████╔╝╚██████╔╝███████╗███████║███████║██║██║ ╚████║╚██████╔╝    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                                                                                                                  '''

print(logo)
print("Wecome to The NUMBER GUESSING GAME!")
print("The Number Can be in Between '1' and '100'.")
print("Lets try it!")


def guess_number_game(attempts):
    """This Function is Used to Get Input From User and Test  against NUMBER"""
    print(f"You have {attempts} Attempts to Win!")
    while attempts:
        user_guess = int(input("Make a Guess: "))
        if NUMBER < user_guess:
            print("Too HIGH")
        elif NUMBER > user_guess:
            print("Too LOW")
        elif NUMBER == user_guess:
            print("Guessed Corectly! Yon WON")
        attempts -= 1
        print(f"You have {attempts} Attempts remaining")
        if attempts == 0 and NUMBER != user_guess:
            print("Could Not Guessed! You Lose")


def game_paly():
    difficulty = input("Choase A Difficulty Level. Type 'e' for Easy, or  'm' for Medium or 'h' for Hard").lower()
    if difficulty == "e":
        guess_number_game(12)
    elif difficulty == "m":
        guess_number_game(8)
    elif difficulty == "h":
        guess_number_game(5)
    else:
        print("Invalid Input")


NUMBER = random.randint(1, 100)

while input("Type 'y' to play game or Other alphabet to Exit Game:  ").lower() == "y":
    game_paly()
