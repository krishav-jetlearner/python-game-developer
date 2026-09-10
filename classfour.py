import pgzrun
import random
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
HEIGHT= 500
WIDTH = 500

bee=Actor("bee")
bee.pos = (250,250)
flower=Actor("flower")
flower.pos = (100,0)

def draw():
    screen.blit(("background1"),(0,0))
    bee.draw()
    flower.draw()

def update():
    if keyboard.left:
        bee.x -= 10
    if keyboard.right:
        bee.x += 10
    if keyboard.up:
        bee.y -= 10
    if keyboard.down:
        bee.y += 10
    if bee.colliderect(flower):
        
pgzrun.go()