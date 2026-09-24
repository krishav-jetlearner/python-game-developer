import pgzrun
import random
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
HEIGHT= 500
WIDTH = 500
score = 0

bee=Actor("bee")
bee.pos = (250,250)
flower=Actor("flower")
flower.pos = (100,0)
time = 0
def draw():
    screen.blit(("background1"),(0,0))
    bee.draw()
    flower.draw()
    if time == 60:
       screen.fill("blue")
       screen.draw.text(str(score),(250,250),fontsize = 50,color = (42,231,54))

def time_60():
    global time
    time = 60
clock.schedule(time_60,10)
def update():
    global score
    if keyboard.left:
        bee.x -= 10
    if keyboard.right:
        bee.x += 10
    if keyboard.up:
        bee.y -= 10
    if keyboard.down:
        bee.y += 10
    if bee.colliderect(flower):
        x1 = random.randint(50,450)
        y1 = random.randint(50,450)
        flower.pos = (x1,y1)
        score += 1
pgzrun.go()