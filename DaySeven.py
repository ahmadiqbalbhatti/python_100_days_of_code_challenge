# Here I am going to Create function for Generating Random Word
import random


wordList = ['HELLO', 'WORLD', 'PROPOSED', 'BEEKEEPING', 'LOVER']
stages = ['''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / /
     |
     |___
''',
          '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / /
     |
     |___
''',
          '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
     |___
''',
          '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
     |___
''',
          '''
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
     |___
''',
          '''
      _______
     |/      |
     |      (_)
     |       |
     |      
     |      
     |
     |___
''',
          '''
      _______
     |/      |
     |      (_)
     |      
     |      
     |      
     |
     |___
''',
          '''
      _______
     |/      |
     |      
     |      
     |      
     |      
     |
     |___
'''
          ]
dashedList = []
chosenWord = random.choice(wordList)
for n in range(len(chosenWord)):
    dashedList.append('_')
print(dashedList)
print(chosenWord)
is_game_ends = False
lives = 6
while not is_game_ends:
    guess = input('Guess A Letter: ').upper()
    i = 0
    for char in chosenWord:
        if char == guess:
            dashedList[i] = char
            print("Matched")
        i += 1
    if guess not in chosenWord:
        print(stages[lives])
        lives -= 1
        if lives==0:
            print('You LOSE')
            exit()
    print(dashedList)
    if '_' not in dashedList:
        is_game_ends = True
        print('You WIN')
