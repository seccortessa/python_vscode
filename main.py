def turn_right():
    turn_left()    
    turn_left()    
    turn_left()

def check_coll():
    while front_is_clear():
        move()
        if not wall_on_right():
            turn_right()
            pass
    if wall_on_right():
        turn_left()
    while not (front_is_clear() and wall_on_right()):
        turn_right()
        
        
def move_to_wall():
    while front_is_clear():
        move()
        
        
def go_and_right():
    while not wall_on_right():         
        turn_right()
        move()
        check_coll()

        

while not at_goal():
    if not front_is_clear():
        turn_right()
    else:
        move()
    while wall_on_right():
        if not front_is_clear():
            turn_left()
        else:
            move()
    turn_right()
    
    if  ( not last_four[0]) and (not last_four[1]) and (not last_four[2]) and (not last_four[3])