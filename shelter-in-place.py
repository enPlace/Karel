from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
   move()
   move()
   turn_right()
   move()
   turn_left()
   move()
   pick_beeper()
   turn_around()
   move()
   turn_right()
   move()
   turn_left()
   move()
   move()
   turn_around()
   # add your code here

def turn_right(): 
   turn_left()
   turn_left()
   turn_left()
   
def turn_around(): 
   turn_left()
   turn_left()