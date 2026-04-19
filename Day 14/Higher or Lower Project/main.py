from art import logo, vs
from game_data import data
import random

# Choose random entry from data.
def choose_entries():
    return random.choice(data)

# Ask player for their guess.
def player_input():
    choice = input("Who has the most followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    if choice not in ("a", "b"):
        print("Invalid selection. Please choose again.")
        choice = player_input()
    return choice

# Compare the amount of followers.
def compare_followers(a, b):
    # print(a.get('follower_count'))
    # print(b.get('follower_count'))
    if a.get('follower_count') > b.get('follower_count'):
        # print(a)
        return "a"
    else:
        # print(b)
        return "b"

# Calculate the score.
# def calculate_score(player_choice, more_followers, score):
#     if player_choice == more_followers:
#         score += 1
#         print(f"You're right! Current score: {score}")
#         return score
#     else:
#         print(f"Sorry, that's wrong. Final score: {score}")
#         return score

a = choose_entries()
b = choose_entries()
score = 0

# Game
def game(a, b, score):
    print(logo)
    # a = choose_entries()
    # b = choose_entries()
    # score = 0
    # global INITIAL_SCORE

    # If entries are the same, choose again.
    if a == b:
        # print('entries are the same')
        # print(a, b)
        b = choose_entries()
        # print(a, b)


    print(f"Compare A: {a.get('name')}, {a.get('description')}, {a.get('country')}")
    print(vs)
    print(f"Against B: {b.get('name')}, {b.get('description')}, {b.get('country')}")

    player_choice = player_input()
    # while player_choice not in ("a", "b"):
    #     print("Invalid selection. Please choose again.")
    #     player_input()



    # else:
    #     print("continue")
    # print(player_choice)
    more_followers = compare_followers(a, b)
    # print(more_followers)

    # player_score = calculate_score(player_choice, more_followers, score)

    if player_choice == more_followers:
        score += 1
        print(f"You're right! Current score: {score}")
        a = b
        # print(a)
        b = choose_entries()
        game(a, b, score)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")



    # print(player_score)
    # if player_score > 0:
    #     a = b
    #     print(a)
    #     game()
    # else:
    #     print("game over")

    # if player_choice == more_followers:
    #     print("yes")
    #     score += 1
    #     print(score)
    #     game()
    # # elif player_choice != more_followers:
    # else:
    #     print("no")

game(a, b, score)




# Access dictionary items.
# for names in data:
# for i in data:
# print(data[0])









# If user guesses correctly, correct entry becomes A.

# If user guesses incorrectly, game is over and score is calculated.