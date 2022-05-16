# Calculate the Paint for a Wall
# ========================    Challenge One  ==========================

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


def paint_calculator(height, width, cover):
    number_of_cans = round((height * width) / cover)
    return number_of_cans


# inputHeight = float(input('Height of the Wall: '))
# inputWidth = float(input('Width of the Wall: '))
# coverage = 5
#
# totalPaint = paint_calculator(height=inputHeight, width=inputWidth,
#                               cover=coverage)
# print('Total Number of Can You Need: ', str(totalPaint))

# =========================    Challenge Two ==========================
# To Find Prime Number

# function that will find prime number
def prime_number(input_number):
    flag = True
    for n in range(2, input_number):
        if input_number % n == 0:
            flag = False
    if flag is not False:
        print(f'{input_number} is a Prime Number')
    else:
        print('Not a prime Number')


# inputNumber = int(input('Enter a Number : '))
# prime_number(input_number=inputNumber)

# ============== Stage 1
# =====================================================================
# ==============   Final Challenge Using Loops  =======================
# =====================================================================
# Caesar Cipher
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
             'y', 'z']


def encrypt(text, shift):
    encrypted_text = ""
    for txt in text:
        i = 0
        for letter in alphabets:
            if txt == letter:
                i += shift
                if i > 25:
                    i -= 26
                for n in range(len(alphabets)):
                    if i == n:
                        print(i)
                        encrypted_text += alphabets[i]
            i += 1
    print(encrypted_text)


def decrypt(text, shift):
    decrypted_text = ""
    for txt in text:
        j = 0  # used to check the index for shift
        for letter in alphabets:
            if txt == letter:
                j = j - shift
                if j < 0:
                    j = 26 + j
                for n in range(len(alphabets)):
                    if j == n:
                        decrypted_text += alphabets[j]
            j += 1
    print(decrypted_text)


# direction = input('Type encode to Encrypt Message or Type '
#                   'decode to decrypt \n').lower()
# inputText = input('Type Text\n').lower()
# inputShift = int(input('give Encode or Decode Number\n'))
#
# if direction == 'encode':
#     encrypt(inputText, inputShift)
# elif direction == 'decode':
#     decrypt(inputText, inputShift)
# else:
#     print('Please chose correct one')


# ============== Stage 2
# =====================================================================
# ============   Final Challenge Using Built In Functions  ============
# =====================================================================

def new_encoder(text, shift):
    ciphertext = ''
    for letter in text:
        index = alphabets.index(letter)
        new_index = index + shift
        if new_index > 25:
            new_index = new_index - 26
        new_letter = alphabets[new_index]
        ciphertext += new_letter
    print(f'My cipher text is {ciphertext}')


def new_decoder(text, shift):
    ciphertext = ''
    for letter in text:
        index = alphabets.index(letter)
        new_index = index - shift
        if new_index < 0:
            new_index = 26 + new_index
        new_letter = alphabets[new_index]
        ciphertext += new_letter
    print(f'My cipher text is {ciphertext}')


# direction = input('Type encode to Encrypt Message or Type '
#                   'decode to decrypt \n').lower()
# inputText = input('Type Text\n').lower()
# inputShift = int(input('give Encode or Decode Number\n'))
#
# if direction == 'encode':
#     encrypt(inputText, inputShift)
# elif direction == 'decode':
#     decrypt(inputText, inputShift)
# else:
#     print('Please chose correct one')


# ============== Stage 3
# =====================================================================
# =======  Try to combine the above two function in one  ==============
# =====================================================================
new_alphabets_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y', 'z',
                      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y', 'z',
                      ]


def caeser_cipher(text, shift, _direction):
    global new_indexes
    ciphertext = ''
    for letter in text:
        if letter in new_alphabets_list:
            index = new_alphabets_list.index(letter)
            if shift > 26:
                shift = shift % 26
            if _direction == 'encode':
                new_indexes = index + shift
            elif _direction == 'decode':
                new_indexes = index - shift
            else:
                print('Please chose correct one')
            new_letter = new_alphabets_list[new_indexes]
            ciphertext += new_letter
        else:
            ciphertext += letter
    print(f'My cipher text is {ciphertext}')


print(logo)
run = False
while not run:
    direction = input('Type encode to Encrypt Message or Type '
                      'decode to decrypt \n').lower()
    inputText = input('Type Text\n').lower()
    inputShift = int(input('give Encode or Decode Number\n'))
    caeser_cipher(text=inputText, shift=inputShift, _direction=direction)
    loopIt = int(input('Type "1" to run task again and "o" to Exit  '))
    if loopIt == 1:
        run = False
    else:
        print('Good By')
        exit()
