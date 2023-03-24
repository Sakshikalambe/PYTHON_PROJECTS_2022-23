from turtle import Turtle, Screen
tim=Turtle()
screen = Screen()


def move_forward():
    tim.forward(30)

def move_backward():
    tim.backward(10)

def move_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)

def move_right():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="W", fun=move_forward)
screen.onkey(key="S", fun=move_backward)
screen.onkey(key="A", fun=move_left)
screen.onkey(key="D", fun=move_left)
screen.onkey(clear,"C")
screen.exitonclick()