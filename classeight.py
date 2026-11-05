import pgzrun
import os
import random
WIDTH = 1150
HEIGHT = 650
level = 1
end_level = 5
num = 0
actors = ["batteryimg","bottleimg","chipsimg","plasticimg"]

os.environ['SDL_VIDEO_CENTERED'] = '1'
def draw():
    screen.blit(("background2"),(0,0))
def make_actors():
    global actors, level, num
    level_actor = ["paperimg"]
    num = 0
    while num < level:
        choice_actors = random.choice(actors)
        level_actor.append(choice_actors)
        num += 1

pgzrun.go()