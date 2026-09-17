import random
import pgzrun
WIDTH = 500
HEIGHT = 500
apple = Actor("apple")
basket = Actor("basket")
apple.pos = (250,50)
basket.pos = (0,400)
score = 0
time = 0
def time_60():
    global time
    time = 60
clock.schedule(time_60,10)
def draw():
   global score
   screen.clear()
   apple.draw()
   basket.draw()
   screen.draw.text(str(score),(450,50),fontsize = 30,color = (45,7,98))
   if time == 60:
       basket.pos = (-5000000000,5000000000000000000000000)
       screen.fill("red")
       screen.draw.text(str(score),(250,250),fontsize = 50,color = (42,231,54))

   
  

def update():
    global score
    if keyboard.left:

        basket.x -= 10

    if keyboard.right:
       basket.x += 10 
    speed = random.uniform(1,5)
    apple.y += speed
    if apple.y >= 500:
        x1 = random.randint(50,450) 
        apple.pos = (x1,50)
    if apple.colliderect(basket):
        x2 = random.randint(50,450)
        score += 1
        apple.pos = (x2,50)



pgzrun.go()