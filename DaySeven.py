
# Here I am going to Create function for Generating Random Word
import random

wordList = ['HELLO', 'WORLD', 'PROPOSED', 'BEEKEEPING', 'LOVER']
chosenWord = random.choice(wordList)
print(chosenWord)
guess = input('Guess A Letter: ').upper()

for char in chosenWord:
    if char == guess:
        print("Matched")
    else:
        print('Wrong')
