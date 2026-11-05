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
score = 0
gameover = False
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
    if gameover == True:
        screen.draw.textbox((str(score)),questionbar,color = ("black"),shadow = (1,1),scolor = ("grey"))
        screen.draw.filled_rect((toprect),("green"))
        screen.draw.textbox(("You finished"),toprect,color = ("black"),shadow = (1,1),scolor = ("grey"))


    
    if toprect.x == -500:
        toprect.x = 500

def time_schedule():
    global time
    if time > 0:
        time -= 1
    elif time == 0:
        game_over()
    
    
    
    
def game_over():
    global time, splitted_value, gameover
    time = 0
    splitted_value = ["","","","","","","76"]
    gameover = True
        
    
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
    global score
    if answer_right_top.collidepoint(pos):
        print(splitted_value[5])
        if int(splitted_value[5]) == 3:
            answer_reading()
            score += 1
        else:
            game_over()
    if answer_right_bottom.collidepoint(pos):
        print(splitted_value[5])
        if int(splitted_value[5]) == 4:
            answer_reading()
            score += 1
        else:
            game_over()
    if answer_left_bottom.collidepoint(pos):
        print(type(splitted_value[5]))
        if int(splitted_value[5]) == 2:
            answer_reading()
            score += 1
        else:
            game_over()
    if answer_left_top.collidepoint(pos):
        print(splitted_value[5])
        if int(splitted_value[5]) == 1:
            answer_reading()
            score += 1

    if answer_skipbar.collidepoint(pos):
        answer_reading()
            
def answer_reading():
    global time
    if len(question_1) >= 1:
        reading_list()
        time = 10
    else:
        game_over()

read()
reading_list()

clock.schedule_interval(time_schedule,1)
pgzrun.go()