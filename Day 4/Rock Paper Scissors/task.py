import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock, Paper, Scissors!")
player_choice = int(input("Type 0 for rock, 1 for paper, or 2 for scissors: "))
computer_choice = random.randint(0, 2)

# choice = list[player_choice, computer_choice]
# print(choice)
print(computer_choice)
if player_choice == 0:
# if choice == [0, 0]:
    print("You chose: " + rock)
    # print(computer_choice)
    if computer_choice == 0:
        print("Computer chose: " + rock)
        print("It's a tie!")
    elif computer_choice == 1:
        print("Computer chose: " + paper)
        print("Computer wins!")
    elif computer_choice == 2:
        print("Computer chose: " + scissors)
        print("You win!")
elif player_choice == 1:
    print("You chose: " + paper)
    if computer_choice == 0:
        print("Computer chose: " + rock)
        print("You win!")
    elif computer_choice == 1:
        print("Computer chose: " + paper)
        print("It's a tie!")
    elif computer_choice == 2:
        print("Computer chose: " + scissors)
        print("Computer wins!")
elif player_choice == 2:
    print("You chose: " + scissors)
    if computer_choice == 0:
        print("Computer chose: " + rock)
        print("Computer wins!")
    elif computer_choice == 1:
        print("Computer chose: " + paper)
        print("You win!")
    elif computer_choice == 2:
        print("Computer chose: " + scissors)
        print("It's a tie!")
# else:
#     print("The match is a tie.")
