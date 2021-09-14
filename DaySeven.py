# Here I am going to Create function for Generating Random Word
import random
from DaySevenHangmanArts import logo
from DaySevenHangmanWords import wordList
from DaySevenHangmanArts import stages
print(logo)
chosenWord = random.choice(wordList)
dashedList = []
for n in range(len(chosenWord)):
    dashedList.append('_')

print(dashedList)
# print(chosenWord)
is_game_ends = False


lives = len(stages)
while not is_game_ends:
    guess = input('Guess A Letter: ').lower()
    if guess in dashedList:
        print('Already Guessed! Please Try Something Else')
    i = 0
    for char in chosenWord:
        if char == guess:
            dashedList[i] = char
        i += 1
    if guess not in chosenWord:
        print('Chosen letter is not in the world! Please THINK and '
              'Try Again')
        lives -= 1
        if lives == 0:
            print(stages[lives])
            print('You LOSE')
            exit()
    print(dashedList)
    if '_' not in dashedList:
        is_game_ends = True
        if lives == 6:
            print('Excellent! You WIN')
        elif lives == 4:
            print('Good! You WIN')
        else:
            print('You WIN')
    print(stages[lives])