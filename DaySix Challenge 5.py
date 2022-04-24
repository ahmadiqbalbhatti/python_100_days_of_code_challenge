# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        # if wall_in_front():
        #    turn_left()
        move()

    right()
    move()
    right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
