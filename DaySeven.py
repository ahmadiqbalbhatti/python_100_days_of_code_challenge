
# Here I am going to Create function for Generating Random Word
import random

wordList = ['HELLO', 'WORLD', 'PROPOSED', 'BEEKEEPING']
chosedWord = random.choice(wordList)
print(chosedWord)
guess = input('Guess A Word: ').lower()
for char in chosedWord:
    if char == guess:
        print(char)
    else:
        print("No match")
