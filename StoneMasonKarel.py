# 1. Knowing that the columns will always start in row one, we know
# that Karel will never have to check to see if there are any extra
# spaces to its south. 

# 2. Each column however, can extend further north than the previous
# column, so each time we move to a new column from a northern
# position, we must check to see if the next column will extend
# further north. If so, we move north, fill the column, turn around,
# and impliment the south column building function

# 3. Because each column can also be shorter than the previous column,
# we can also run into a situation where karels path is blocked while
# trying to move to the next column, so we must also implement a
# function to follow the shape of the ceiling until we can get to the
# next column position. 



def main():
    turn_left()
    build_north_column()


def turn_right(): 
    turn_left()
    turn_left()
    turn_left()

def turn_around(): 
    turn_left()
    turn_left()

def check_left(): 
    if left_is_clear(): 
        turn_left() 
        build_column()
        turn_around()

        
def move_four():
    for i in range(4):
        if front_is_clear(): 
            move()
        elif front_is_blocked():
            turn_right()
            while left_is_blocked():
                move()
            if left_is_clear():
                turn_left()
                move()
                

def build_column(): 
    if no_beepers_present():
        put_beeper()
    move()

def build_north_column():
    while front_is_clear(): 
        build_column()
    if front_is_blocked():
        if no_beepers_present():
            put_beeper() 
        turn_right()
        if front_is_clear():
            move_four()
            check_left()
            build_south_column()

def build_south_column():
    if facing_east():
        turn_right()
    while front_is_clear():
        build_column()
    if front_is_blocked():
        turn_left()
        if front_is_clear(): 
            move_four()
            turn_left()
            build_north_column()


