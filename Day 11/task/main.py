import random
from art import logo
print(logo)
# play_choice = ""
# play_choice = input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no.\n").lower
# if play_choice == "y":
# print(play_choice)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards = [11, 10, 11]
# print(cards)
# elif play_choice == "n":
# else:
#     print("Goodbye!")

deal_player = 2
deal_computer = 2
player_hand = []
computer_hand = []
get_another_card = ""
player_blackjack = False
computer_blackjack = False
# player_turn = False
# computer_turn = False
# player_score = sum(player_hand)
# computer_score = sum(computer_hand)
# hit_me = True

# def deal_card():
#     # player_hand == random.choice(cards)
#     # print(player_hand)
#     return random.choice()
#     card_choice = random.choice(cards)
#     print(card_choice)
#     print("\n")
#     return card_choice
# deal_card()

def deal_card(cards):
    return random.choice(cards)
deal_card(cards)

# def get_score(player_hand, computer_hand):
#     player_score = sum(player_hand)
#     computer_score = sum(computer_hand)
#     return player_score and computer_score

def hit(player_score, computer_score):
    get_another_card = input("Type 'y' to hit, or 'n' to stand:").lower()
    if get_another_card == "n":
        stand(player_score, computer_score)
    else:
    # if get_another_card == "y":
        player_hand.append(deal_card(cards))
        # print(player_hand)
        player_score = sum(player_hand)
        print(f"You cards: {player_hand}, current score is {player_score}.")
        print(f"Computer's first card: {computer_hand[0]}")
        # print(player_score)
        if player_score > 21:
            # if player_hand.index(11):
            #     player_hand.remove(11)
            #     player_hand.append(1)
            #     print(player_hand)
            #     player_score = sum(player_hand)
            #     # hit(player_score, computer_score)
            # else:
            stand(player_score, computer_score)
        # return player_hand
        else:
            hit(player_score, computer_score)
    # else:
    #     hit(player_score)
    # if get_another_card == "y":
    #     hit(player_score)
    # else:
    #     stand(player_score)

def stand(player_score, computer_score):
    #     while computer_score != 0:
    if player_blackjack == True:
        print(f"Your final hand: {player_hand}, your final score is Blackjack!")
    else:
        print(f"Your final hand: {player_hand}, your final score is {player_score}.")
    if computer_blackjack == True:
        print(f"Computer's final hand: {computer_hand}, computer's final score is Blackjack.\n")
    else:
    # print(computer_score)
        while computer_score < 17:
            computer_hand.append(deal_card(cards))
            # print(computer_hand)
            computer_score = sum(computer_hand)
            # print(computer_score)

        print(f"Computer's final hand: {computer_hand}, computer's final score is {computer_score}.\n")


    if player_score > 21 and computer_score > 21:
        # print(player_score, computer_score)
        print("You both bust! You lose!")
    elif player_score <= 21 and computer_score > 21:
        if player_blackjack == True:
            # print(player_score, computer_score)
            print("Blackjack! Computer busts! You win!")
        else:
            # print(player_score, computer_score)
            print("Computer busts! You win!")
    elif player_score > 21 and computer_score <= 21:
        if computer_blackjack == True:
            print("Bust! Computer has Blackjack! You lose!")
        else:
            print("Bust! You lose!")

    # elif player_score > 21 and computer_score > 21:
    #     print("You both bust, but you lose your bet.")
    # # elif computer_score <= 21
    #         elif computer_score <= 21:
    #             if computer_score == 21:
    #                 print("Computer gets 21")
    #             elif computer_score < 21:
    #                 if computer_score <= 16:
    #                     computer_hand.append(deal_card(cards))
    elif player_score == computer_score:
        if player_blackjack == True and computer_blackjack == False:
            # print(player_hand)
            print("Blackjack! You win!")
        elif player_blackjack == False and computer_blackjack == True:
            # print(computer_hand)
            print("Blackjack! Computer wins!")
        else:
            # print(player_score, computer_score)
            print("Push!")
    elif player_score < computer_score:
        if computer_blackjack == True:
            # print(computer_hand)
        # if player_score < 21 and computer_score == 21:
            print("Blackjack! Computer wins!")
        else:
            # print(player_score, computer_score)
            print("Computer wins!")
    elif player_score > computer_score:
        if player_blackjack == True:
        # if player_score == 21 and computer_score < 21:
        #     print(player_hand)
            print("Blackjack! You win!")
        else:
            # print(player_score, computer_score)
            print("You win!")

    # elif player_score <= 21:
    #     if player_score == computer_score:
    #         print(computer_score)
    #         print("Draw!")
    #     elif player_score < computer_score:
    #         print(computer_score)
    #         print("Computer wins!")
    #     elif player_score > computer_score:
    #         print(computer_score)
    #         print("You win!")
    # else:
    #     print(computer_score)
    #     print("You bust!")
    #     return
    # else:
    #     while computer_score != 0:
    #         if computer_score > 21:
    #             print("Computer busts!")
    #         elif computer_score <= 21:
    #             if computer_score == 21:
    #                 print("Computer gets 21")
    #             elif computer_score < 21:
    #                 if computer_score <= 16:
    #                     computer_hand.append(deal_card(cards))




# while player_hand == []:
while deal_player != 0 and deal_computer != 0:
    player_hand.append(deal_card(cards))
    computer_hand.append(deal_card(cards))
    deal_player -= 1
    deal_computer -= 1
    player_score = sum(player_hand)
    computer_score = sum(computer_hand)
if player_score == 21:
    player_blackjack = True
    if computer_score == 21:
        computer_blackjack = True
    print(f"Your cards: {player_hand}, you have Blackjack!")
    print(f"Computer's first card: {computer_hand[0]}")
    stand(player_score, computer_score)
    # elif computer_score == 21:
    #     computer_blackjack = True
    #     print(f"You cards: {player_hand}, current score is {player_score}.")
    #     print(f"Computer's first card: {computer_hand[0]}")
    #     hit(player_score, computer_score)
else:
    if player_score > 21:
        print(player_hand)
        if player_hand[1] == 11:
            player_hand.remove(11)
            print(player_hand)
            player_hand.append(1)
            print(player_hand)
            player_score = sum(player_hand)
    if computer_score > 21:
        if computer_hand[1] == 11:
            computer_hand.remove(11)
            computer_hand.append(1)
            print(computer_hand)
            computer_score = sum(computer_hand)
    if computer_score == 21:
        computer_blackjack = True
    print(f"Your cards: {player_hand}, current score is {player_score}.")
    print(f"Computer's first card: {computer_hand[0]}")
    hit(player_score, computer_score)
# else:
    # get_score(player_hand, computer_hand)

    # print(player_hand)
    # print(computer_hand)
    # if player_hand == [11, 11]:
    #     player_hand == [11, 1]
    #     print(player_hand)
    # print(deal_player)

# get_another_card = input("Type 'y' to hit, or 'n' to stand: ").lower()

#     # hit_me = True
#     while hit_me == True:


# hit(player_score, computer_score)
#
# if get_another_card == "y":
#     hit(player_score)
# else:
#     stand(player_score)



# else:
#     hit_me = False

# get_another_card = input("Type 'y' to hit, or 'n' to stand: ")
#
# while hit_me == True:
#     hit_()
#
#
#
# while another_card == "y":
#     player_hand.append(deal_card(cards))
#     if player_score < 21:



# def play_game(player_score, computer_score):
    # if player_turn == False:
# computer_hand.append(deal_card(cards))



# elif computer_score < 16:
#     computer_hand.append(deal_card(cards))
    # play_game(player_score, computer_score)
# print(computer_hand)
# print(sum(computer_hand))

# play_game(player_score, computer_score)

# def deal_hand(cards, player_hand, computer_hand, deal_player, deal_computer):
#     player_card1 = 0
#     player_card2 = 0
#     computer_card1 = 0
#     computer_card2 = 0
#     # player_hand = ["", ""]
#     while deal_player == 2:
#         player_hand = random.choice(cards)
#         deal_player -= 1
#         print(player_hand)
#         print(deal_player)
#     while player_hand == []:
#         player_hand = random.choice(cards)
#     while player_card1 == 0 and player_card2 == 0:
#         player_card1 = random.choice(cards)
#         player_card2 = random.choice(cards)
#     while computer_card1 == 0 and computer_card2 == 0:
#         computer_card1 = random.choice(cards)
#         computer_card2 = random.choice(cards)
#     print(player_card1)
#     print(player_card2)
#     print(computer_card1)
#     print(computer_card2)
#     # print(player_hand)
#     # print(random.choice(cards))
# deal_hand(cards, player_hand, computer_hand, deal_player, deal_computer)


# while deal == 2:
#     deal_card(cards)
#     deal += 1
#     print(deal)