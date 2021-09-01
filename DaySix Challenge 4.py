# use the commented link to implement the code in fornt of you
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    #turn_right()
    #if front_is_clear():
    #    move()
    #    if not wall_in_front():
    #        turn_right()
    #elif not front_is_clear():
    #    turn_left()
    if front_is_clear():
        move()
    else:
        jump()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
