# Calculate the Paint for a Wall
# ========================    Challenge One  ==========================

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
        index = new_alphabets_list.index(letter)
        if _direction == 'encode':
            new_indexes = index + shift
        elif _direction == 'decode':
            new_indexes = index - shift
        else:
            print('Please chose correct one')
        new_letter = new_alphabets_list[new_indexes]
        ciphertext += new_letter
    print(f'My cipher text is {ciphertext}')


direction = input('Type encode to Encrypt Message or Type '
                  'decode to decrypt \n').lower()
inputText = input('Type Text\n').lower()
inputShift = int(input('give Encode or Decode Number\n'))

caeser_cipher(text=inputText, shift=inputShift, _direction=direction)
