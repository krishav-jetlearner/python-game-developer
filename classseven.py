import pgzrun
import random
WIDTH = 500
HEIGHT = 500
toprect= Rect(0,0,500,50)
questionbar = Rect(60,100,350,50)
answer_left_top = Rect(60,160,170,100)
answer_left_bottom = Rect(60,280,170,100)
answer_right_top = Rect(250,160,170,100)
answer_right_bottom = Rect(250,280,170,100)
answer_skipbar = Rect(440,160,50,200)
timer = Rect(430,100,50,50)
time = 10
question_1 = []
splited_value = []
def draw():
    screen.clear()
    screen.draw.filled_rect((toprect),("green")) 
    screen.draw.filled_rect((questionbar),("blue"))
    screen.draw.filled_rect((answer_left_top),("orange"))
    screen.draw.filled_rect((answer_left_bottom),("orange"))
    screen.draw.filled_rect((answer_right_top),("orange"))
    screen.draw.filled_rect((answer_skipbar),("red"))
    screen.draw.filled_rect((timer),("yellow"))
    screen.draw.filled_rect((answer_right_bottom),("orange"))
    screen.draw.textbox(("Welcome to quizmaster"),toprect,color = ("black"),shadow = (1,1),scolor = ("grey"))
    screen.draw.textbox(("Skip"),answer_skipbar,color = ("black"),angle = 90,shadow = (1,1),scolor = ("grey"))
    screen.draw.textbox((str(time)),timer,color = ("black"),shadow = (1,1),scolor = ("grey"))
    screen.draw.textbox((splitted_value[0]),questionbar,color = ("black"),shadow = (1,1),scolor = ("grey"))
    screen.draw.textbox((splitted_value[1]),answer_left_top,color = ("black"),shadow  = (1,1),scolor = ("grey"))
    screen.draw.textbox((splitted_value[2]),answer_left_bottom,color = ("black"),shadow = (1,1),scolor = ("grey"))
    screen.draw.textbox((splitted_value[3]),answer_right_top,color = ("black"),shadow = (1,1),scolor = ("grey"))
    screen.draw.textbox((splitted_value[4]),answer_right_bottom,color = ("black"),shadow = (1,1),scolor = ("grey"))
    if toprect.x == -500:
        toprect.x = 500

def time_schedule():
    global time
    if time > 0:
        time -= 1
    
def game_over():
    global time
    time = 0
def read():
    global question_1
    file = open(r"C:\Users\ahuja\OneDrive\Desktop\coding\python game developer\quizmaster\questionclass.txt","r")
    for i in file:
        question_1.append(i)

def reading_list():
    global question_1, splitted_value
    random.shuffle(question_1)
    deleted_value = question_1.pop(0)
    splitted_value = deleted_value.split(",")
def on_mouse_down(pos):
    pass
read()
reading_list()
print(splitted_value)
clock.schedule_interval(time_schedule,1)
pgzrun.go()