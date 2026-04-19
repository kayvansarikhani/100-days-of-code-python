# import another_module
# from another_module import another_variable
#
# print(another_variable)
# print(another_module.another_variable)
# from turtle import Turtle, Screen
# timmy = Turtle()
# my_screen = Screen()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("chartreuse")
# timmy.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()
from traceback import clear_frames

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align =  "l"


print(table)