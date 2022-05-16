# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# steps = 1
# while steps<=6:
#    if at_goal():
#        print("We have read the Our Destination")
#    else:
#        jump()
#    steps +=1

while not at_goal():
    jump()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
