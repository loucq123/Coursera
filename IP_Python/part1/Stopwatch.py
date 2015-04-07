# template for "Stopwatch: The Game"

# define global variables
import simplegui

walkTime = 0
interval = 100
successNumber = 0
tryNumber = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minute = str(t // 600)
    seconds = str((t % 600) // 10)
    rest = str(t % 10)
    return minute + ":" + seconds + "." + rest
        
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def end():
    global successNumber, tryNumber
    if timer.is_running():
        timer.stop()
        if walkTime % 10 == 0:
            successNumber += 1
        tryNumber += 1

def reset():
    global walkTime, successNumber, tryNumber
    walkTime = 0
    timer.stop()
    successNumber = 0
    tryNumber = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global walkTime
    walkTime += 1

# define draw handler
def draw(canvas):
    record = str(successNumber) + "/" + str(tryNumber)
    canvas.draw_text(record, [150,25], 30, "Green")
    canvas.draw_text(format(walkTime), [45,110], 40, "White")
    
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)

# register event handlers
frame.add_button("start", start, 100)
frame.add_button("end", end, 100)
frame.add_button("reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)
# start frame
frame.start()
# Please remember to review the grading rubric
