__Author__ = 'Loucq'

# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global deck, exposed, indexOfCard1, indexOfCard2, CARDWIDTH, CARDHEIGHT, state, counter
    CARDWIDTH = 50
    CARDHEIGHT = 100
    deck = [0, 1, 2, 3, 4, 5, 6, 7] * 2
    random.shuffle(deck)
    exposed = [False] * 16
    indexOfCard1 = None
    indexOfCard2 = None
    state = 0
    counter = 0
    label.set_text("Turns = 0" )


# define event handlers
def mouseclick(pos):
    global deck, exposed, indexOfCard1, indexOfCard2, CARDWIDTH, CARDHEIGHT, state, counter
    index = pos[0] // 50
    if state == 0:
        indexOfCard1 = index
        exposed[indexOfCard1] = True
        state += 1
    elif not exposed[index]:
        if state == 1:
            indexOfCard2 = index
            exposed[indexOfCard2] = True
            if deck[indexOfCard1] == deck[indexOfCard2]:
                state = 0
            else:
                state += 1
        else:
            state = 0
            exposed[indexOfCard1], exposed[indexOfCard2] = False, False
            counter += 1
            label.set_text("Turns = " + str(counter))



# cards are logically 50x100 pixels in size
def draw(canvas):
    global deck, exposed, indexOfCard1, indexOfCard2, CARDWIDTH, CARDHEIGHT, state
    for number in range(16):
        if exposed[number]:
            canvas.draw_text(str(deck[number]), [3 + CARDWIDTH*number, 85], 90, "White")
        else:
            canvas.draw_polygon([[CARDWIDTH * number, CARDHEIGHT],
                                 [CARDWIDTH * number, 0],
                                 [CARDWIDTH + CARDWIDTH * number, 0],
                                 [CARDWIDTH + CARDWIDTH * number, CARDHEIGHT]],
                                1, 'Brown', 'Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric