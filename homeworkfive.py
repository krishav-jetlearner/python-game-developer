import pgzrun
WIDTH = 500
HEIGHT = 500
toprect = Rect(0,0,500,50)
questionbar = Rect(60,100,350,50)
skipbar = Rect(400,160,90,200)
answer_left = Rect(40,160,350,100)
answer_right = Rect(40,280,350,100)
timer = Rect(430,100,50,50)
time = 10
def draw():
    screen.draw.filled_rect((toprect),("white"))
    screen.draw.filled_rect((questionbar),("blue"))
    screen.draw.filled_rect((skipbar),("green"))
    screen.draw.filled_rect((answer_left),("red"))
    screen.draw.filled_rect((answer_right),("red"))
    screen.draw.filled_rect((timer),("yellow"))
    screen.draw.textbox(("Welcome to quizmaster"),toprect,color = ("black"),shadow = (1,1),scolor = ("grey"))
    screen.draw.textbox(("Skip"),skipbar,color = ("black"),angle = 90,shadow = (1,1),scolor = ("grey"))
    screen.draw.textbox((str(time)),timer,color = ("black"),shadow = (1,1),scolor = ("grey"))
def update():
    toprect.x -= 2
    if toprect.x == -500:
        toprect.x = 500

def time_schedule():
    global time
    if time > 0:
        time -= 1
def game_over():
    global time
    time = 0

clock.schedule_interval(time_schedule,1)
pgzrun.go()