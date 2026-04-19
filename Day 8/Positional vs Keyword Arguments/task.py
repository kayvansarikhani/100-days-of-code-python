# # Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# Functions with more than one input

name = input("What is your name?\n")
location = input("Where are you at?\n")

def greet_with(name, location):
    print("Hello " + name + "!")
    print("What's it like in " + location + "?")

greet_with(name, location)
greet_with(location, name)