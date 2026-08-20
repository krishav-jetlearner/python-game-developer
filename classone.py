import pgzrun

WIDTH = 300
HEIGHT = 200
width = 80
height = 100
def draw():
    global width,height
    for i in range(10):
        rectangle = Rect((100,100),(width,height))
        rectangle.center = (150,100)
        screen.draw.rect((rectangle),(0,0,235))
        width -= 8
        height -= 10
    
pgzrun.go()