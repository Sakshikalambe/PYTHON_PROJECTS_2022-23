# import turtle
# https://docs.python.org/3/library/turtle.html
#
# import other
# print(other.other_value)
#
# from turtle import Turtle, Screen
# saku=Turtle()
# print(saku)
# saku.shape("turtle")
# saku.color("Blue")
# saku.forward(100)
# saku.left(50)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="c"
print(table)


