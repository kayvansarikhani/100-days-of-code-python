print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
direction = input("Left or Right? ")
if direction == "Left" or direction == "left":
# if input("Left or right? ") == "Left" or "left":
    print("You arrive at a lake. Do you want to swim or wait?")
    action = input("Swim or Wait? ")
    if action == "Wait" or action == "wait":
        print("A boat arrives and ferries you across the lake. You arrive at three doors: one red, one yellow, "
              "and one blue.")
        door = input("Which door do you want to try? ")
        if door == "Red" or door == "red":
            print("As you open the door, flames engulf you and burn you to cinders. Game over!")
        elif door == "Blue" or door == "blue":
            print("As you open the blue door, hungry wolves attack and devour you. Game over!")
        elif door == "Yellow" or door == "yellow":
            print("You find the treasure chest! Congratulations!")
        else:
            print("That's not valid. Game over!")
    elif action == "Swim" or action == "swim":
        print("You are attacked by an aggressive trout and die. The end!")
elif direction == "Right" or direction == "right":
    print("You are lost in the jungle and die. Game over!")
else:
    print("That's not valid.")