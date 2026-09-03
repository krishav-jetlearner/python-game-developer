import pgzrun
import random


WIDTH = 500
HEIGHT = 550
TITLE = "Game"
cat = Actor("cat")

message =""
def draw():
    #screen.fill(color = (234,46,90))
    x = random.randint(0,450)
    y = random.randint(0,500)
    cat.pos = (x,y)
    screen.clear()
    cat.draw()
    screen.draw.text(message,center = (50,50),fontsize = 30,color = (234,90,45))
    print(x,y)
def on_mouse_down(pos):
    global message
    if cat.collidepoint(pos):
        x1 = random.randint(0,450)
        y1 = random.randint(0,500)
        cat.pos = (x1,y1)
        message = "good shot"
    else:
        message = "missed"
pgzrun.go()