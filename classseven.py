import pgzrun
WIDTH = 500
HEIGHT = 500
toprect= Rect(0,0,500,50)
questionbar = Rect(60,100,350,50)
answer_left_top = Rect(120,160,100,75)

def draw():
    screen.draw.filled_rect((toprect),("green")) 
    screen.draw.filled_rect((questionbar),("blue"))
    screen.draw.filled_rect((answer_left_top),("orange"))
pgzrun.go()