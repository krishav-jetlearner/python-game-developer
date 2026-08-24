import pgzrun
import random
WIDTH = 300
HEIGHT = 200
width = 160
height = 160
radius = 150

def draw():
    global width,height,radius
    for i in range(10):
        r = random.randint(0,235)
        g = random.randint(0,235)
        b = random.randint(0,235)
        r1 = random.randint(0,235)
        g1 = random.randint(0,235)
        b1 = random.randint(0,235)
        rectangle = Rect((0,0),(width,height))
        rectangle.center = (150,100)
        screen.draw.rect((rectangle),(r,g,b))
        screen.draw.circle((150,100),(radius),(r1,g1,b1))
        width -= 16
        height -= 16
        radius -= 15
pgzrun.go()
