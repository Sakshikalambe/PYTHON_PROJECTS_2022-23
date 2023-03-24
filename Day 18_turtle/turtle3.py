import turtle as t
import random
tim=t.Turtle()

colors = ["orchid","deep pink","crimson","dark red","sienna","chartreuse","medium sea green","dark turquoise"]
def draw_shape(num_sides):
    for i in range(num_sides):
        angle=360/num_sides
        t.forward(100)
        t.right(angle)

for shape_side_n in range(3,11):
    t.color(random.choice(colors))
    draw_shape((shape_side_n))


