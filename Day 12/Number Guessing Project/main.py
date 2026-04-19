from art import logo
import random
print(logo)

# Set Difficulty
def difficulty():
    difficulty_setting = input("Choose a difficulty. Type 'easy' for easy, or 'hard' for hard:\n").lower()
    if difficulty_setting == "easy":
        attempts = 9
        print("You have 10 guesses.")
    else:
        attempts = 4
        print("You have 5 guesses.")
    return attempts

# number_of_guesses = difficulty()
# print(number_of_guesses)

# Set Random Number
def set_number():
    return random.randint(0, 101)

# number_to_guess = set_number()
# print(number_to_guess)

# Get User Input
def guess_a_number(guess_again):
    # guess_again = False
    if guess_again == False:
        guess = int(input("Make a guess: "))
        # print(guess_again)


        # return guess
    else:
    # elif guess_again == True:
        guess = int(input("Incorrect! Guess again: "))
        # return guess
    # guess_again = True
    # print(guess_again)
    return guess

# player_choice = guess_a_number()
# print(player_choice)

# Compare Numbers (Too Low or Too High)
# def compare_numbers(number_of_guesses, number_to_guess, player_choice):
# def compare_numbers(number_of_guesses, number_to_guess):
def play_game():
    print("Welcome to Guess the Number!\n")
    number_of_guesses = difficulty()
    print("I'm thinking of a number between 1 to 100.\n")
    number_to_guess = set_number()
    # print(number_to_guess)
    guess_again = False
    player_choice = guess_a_number(guess_again)
    # print(player_choice[1])
    while number_of_guesses:
        if number_to_guess > player_choice:
            print("Too low.")
            number_of_guesses -= 1
            # print(number_of_guesses)
            guess_again = True
            player_choice = guess_a_number(guess_again)
        elif number_to_guess < player_choice:
            print("Too high.")
            number_of_guesses -= 1
            # print(number_of_guesses)
            guess_again = True
            player_choice = guess_a_number(guess_again)
        elif number_to_guess == player_choice:
            print(number_of_guesses)
            return True
        # return player_choice
        # guess_a_number()
        # print(player_choice)
        # print(number_of_guesses, number_to_guess, player_choice)

# result = compare_numbers(number_of_guesses, number_to_guess, player_choice)
# result = compare_numbers(number_of_guesses, number_to_guess)
result = play_game()
# print(result)

# Win or Lose
def win_or_lose(result):
    if result is True:
        print("Correct! You win!")
    else:
        print("You have run out of guesses. You lose!")

win_or_lose(result)