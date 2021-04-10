# This is an editor! An editor is where you write code.
# Make karel: move, turn_left, move
def main():
   turn_left()
   move()
   turn_right()
   for i in range(2): 
      drop_five()
   for i in range(2): 
      drop_four()
   # add your code here

def turn_right(): 
   turn_left()
   turn_left()
   turn_left()

def drop_five(): 
   for i in range(5): 
      move()
      put_beeper()
   turn_left()
   
def drop_four(): 
   for i in range(4): 
      move()
      put_beeper()
   turn_left()