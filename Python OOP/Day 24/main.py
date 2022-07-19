# # How to read in the file
# with open("my_text.txt") as file:
#     contents = file.read()
#     print(contents)


# # how to write in the file
with open("my_text.txt", mode="a") as file:
    file.write("Its my new text\n")

with open("new_file.txt", mode="a") as file:
    file.write("I love you\n")

with open("new_other_file.txt", mode="a") as file:
    file.write("I love you\n")