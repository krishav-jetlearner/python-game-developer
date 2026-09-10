import pgzrun
import random


WIDTH = 500
HEIGHT = 550
TITLE = "Game"
cat = Actor("cat")
true = False
message =""
circle = []
x = random.randint(0,450)
y = random.randint(0,500)
def draw():
    
    r = random.randint(0,235)
    g = random.randint(0,235)
    b = random.randint(0,235)
    #screen.fill(color = (234,46,90))
    cat.pos = (x,y)
    screen.clear()
    cat.draw()  
    screen.draw.text(message,center = (50,50),fontsize = 30,color = (234,90,45))
    for i in range(len(circle)):
        
        screen.draw.filled_circle((circle[i]),(5),(r,g,b))

def on_mouse_down(pos):
    global message,true,x,y,circle
    if cat.collidepoint(pos):
        x = random.randint(0,450)
        y = random.randint(0,500)
        cat.pos = (x,y)
        message = "good shot"

        circle.append(pos)
        
    else:
        message = "missed"
        true = False
pgzrun.go()