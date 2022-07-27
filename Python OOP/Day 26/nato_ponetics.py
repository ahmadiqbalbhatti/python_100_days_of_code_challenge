import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
# letters = []
# codes = []
#
# for (index, row) in data.iterrows():
#     letters.append(row.letter)
#     codes.append(row.code)
# print(letters)
# print(codes)
#
#
#     # dict_data2 = {}

# print(data)
# -------- this is how we can convert data frame in to a dictionary using comprehension in one line
# for (index, row) in data.iterrows():
#     dict_data = {row.letter:row.code}

# print(dict_data.keys())


# dict_data = {letter: code for (letter, code) in data for (index, row) in data.iterrows()}

dict_data = {row.letter: row.code for (index, row) in data.iterrows() }

input_word = input("Enter Word : ").upper()

list_of_input_word = [char for char in input_word if not char.__contains__(" ")]
# print(list_of_input_word)


# phonetics = {key: value for (key, value) in dict_data.items()}
# print(phonetics)

for (key, value) in dict_data.items():
    if key in list_of_input_word:
        print(f'{key}: {value}')

# print(list_of_input_word)
# print(dict_data)