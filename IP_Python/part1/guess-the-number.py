# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game
def new_game():
    global trueNumber, steps

# define event handlers for control panel
def range100():
    global trueNumber, steps
    trueNumber = random.randrange(100)
    steps = 7

def range1000():
    global trueNumber, steps
    trueNumber = random.randfrange(1000)
    steps = 10
    
def input_guess(guess):
    global trueNumber, steps
    if steps <= 0:
        print "You ran out guesses. The true number is ", str(trueNumber)
        new_game()
    else:
        if int(guess) > trueNumber:
            print "Higher"
        elif int(guess) < trueNumber:
            print "Lower"
        else:
            print "Correct!"
        steps -= 1
        print "Number of remaining guesses is ", str(steps)
        print 
    
# create frame
frame = simplegui.create_frame("Guess the number!", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("range[0,100)", range100, 200)
frame.add_button("range[0,1000)", range1000, 200)
frame.add_input("enter a guess:", input_guess, 200)

# call new_game 
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
