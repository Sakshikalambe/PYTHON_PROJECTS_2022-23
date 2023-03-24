import random
import turtle as t
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color=(r,g,b)
    return random_color


move=[0,90,180,270]

t.pensize(10)
t.speed(0)
for i in range(200):
    t.color(random_color())
    t.forward(40)
    t.setheading(random.choice(move))