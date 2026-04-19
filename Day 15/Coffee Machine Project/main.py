MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "penny": 0.01,
}

coffee_machine_on = True
enough_resources = True
# not_enough_money = True
profit = 0.00
espresso_ingredients = MENU.get('espresso').get('ingredients')
latte_ingredients = MENU.get('latte').get('ingredients')
cappuccino_ingredients = MENU.get('cappuccino').get('ingredients')
water = resources.get('water')
milk = resources.get('milk')
coffee = resources.get('coffee')

def refill():
    global water, milk, coffee, enough_resources
    print(water, milk, coffee)
    water = 300
    resources.update({'water': water})
    milk = 200
    resources.update({'milk': milk})
    coffee = 100
    resources.update({'coffee': coffee})




    # resources.update({'water': 300})
    # resources.update({'milk': 200})
    # resources.update({'coffee': 100})
    print(resources)
    print(water, milk, coffee)
    enough_resources = True
    # selection = ""
    # user_selection()

# Ask user for their input
def user_selection():
    # selection = ""
    global water, milk, coffee
    print(water, milk, coffee)
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    print(water, milk, coffee)
    if selection == "off":
        turn_off()
    elif selection == "report":
        print_report()
    elif selection == "refill":
        refill()
    elif selection == "espresso":
        order_espresso()
    elif selection == "latte":

        order_latte()
        # selection = ""
    elif selection == "cappuccino":
        order_cappuccino()
    else:
        print("Invalid order. Please try again.")

def order_espresso():
    order = "espresso"
    cost = MENU.get('espresso')['cost']
    check_resources(order)
    # money = round(insert_coins(), 2)
    # check_money(money, cost, order)
    if not enough_resources:
        # selection = ""
        user_selection()
    else:
        money = round(insert_coins(), 2)
        check_money(money, cost, order)


    # if not not_enough_money:
    # #     user_selection()
    # # else:
    #     print("Here is your espresso. Enjoy!")

def order_latte():
    order = "latte"
    cost = MENU.get('latte')['cost']
    check_resources(order)
    if not enough_resources:
        # selection = ""
        user_selection()
    else:
        money = round(insert_coins(), 2)
        check_money(money, cost, order)



    # # else:
    # if not not_enough_money:
    # #     print(not_enough_money)
    #     print("Here is your latte. Enjoy!")

def order_cappuccino():
    order = "cappuccino"
    cost = MENU.get('cappuccino')['cost']
    check_resources(order)
    # money = round(insert_coins(), 2)
    # check_money(money, cost, order)
    if not enough_resources:
        # selection = ""
        user_selection()
    else:
        money = round(insert_coins(), 2)
        check_money(money, cost, order)
    # if not not_enough_money:
    #     print(not_enough_money)
    # else:
    #     print("Here is your cappuccino. Enjoy!")

def turn_off():
    print("\nShutting down. Goodbye!")
    global coffee_machine_on
    coffee_machine_on = False
    return coffee_machine_on

def print_report():
    print(f"\nWater: {resources.get('water')}")
    print(f"Milk: {resources.get('milk')}")
    print(f"Coffee: {resources.get('coffee')}")
    print("Money: $", profit)

def check_resources(order):
    # global enough_resources, espresso_ingredients, latte_ingredients, cappuccino_ingredients
    global resources, water, milk, coffee, enough_resources
    # water = resources.get('water')
    # milk = resources.get('milk')
    # coffee = resources.get('coffee')
    # print(espresso_ingredients)
    # print(latte_ingredients)
    # print(cappuccino_ingredients)
    # print(order)
    # enough_resources = True
    # remaining_water = 0
    # while enough_resources:
    if order == "espresso":
        if espresso_ingredients.get('water') > water and espresso_ingredients.get('coffee') > coffee:
            print("Sorry, there is not enough water or coffee.\n")
            # use_machine()
            enough_resources = False
            # user_selection()
        elif espresso_ingredients.get('water') > water:
            print("Sorry, there is not enough water.\n")
            # use_machine()
            enough_resources = False
            # user_selection()
        elif espresso_ingredients.get('coffee') > coffee:
            print("Sorry, there is not enough coffee.\n")
            # use_machine()
            enough_resources = False
            # user_selection()
        else:
        # if (espresso_ingredients.get('water') <= water and espresso_ingredients.get('coffee') <= coffee):
            water -= espresso_ingredients.get('water')
            resources.update({'water': water})
            coffee -= espresso_ingredients.get('coffee')
            resources.update({'coffee': coffee})
            # water = 40
            # resources.update({'water': water})
            # coffee = 25
            # resources.update({'coffee': coffee})
            # print(water, coffee)

            # enough_resources = False

            # return water, coffee

            # print(water, coffee)
        # elif espresso_ingredients.get('water') > water and espresso_ingredients.get('coffee') > coffee:
        #     print("Sorry, there is not enough water or coffee.\n")
        #     user_selection()
        # elif espresso_ingredients.get('water') > water or espresso_ingredients.get('coffee') > coffee:
        # if espresso_ingredients.get('water') > water:
        #     print("Sorry, there is not enough water.\n")
        #     user_selection()
        # if espresso_ingredients.get('coffee') > coffee:
        #     print("Sorry, there is not enough coffee.\n")
        #     user_selection()

        # elif es
        #     print("Sorry, there is not enough water.")
        #     return
        # print(espresso_ingredients.get('water'))
            # or espresso_ingredients.get('coffee')
    elif order == "latte":

        # print(water, milk, coffee)
        if (latte_ingredients.get('water') > water
            and latte_ingredients.get('milk') > milk
            and latte_ingredients.get('coffee') > coffee
        ):
            print("Sorry, there is not enough water, milk, and coffee.\n")
            enough_resources = False
            # user_selection()
        elif latte_ingredients.get('water') > water:
            print("Sorry, there is not enough water.\n")
            # return user_selection()
            enough_resources = False
            # user_selection() = ""
        elif latte_ingredients.get('milk') > water:
            print("Sorry, there is not enough milk.\n")
            enough_resources = False
            # user_selection()
        elif latte_ingredients.get('coffee') > coffee:
            print("Sorry, there is not enough coffee.\n")
            enough_resources = False
            # user_selection()
        else:
            # print(water, milk, coffee)
        # if (espresso_ingredients.get('water') <= water and espresso_ingredients.get('coffee') <= coffee):
        #
        #     "water": 200,
        #     "milk": 150,
        #     "coffee": 24,

            # resources['water'] -= latte_ingredients.get('water')
            water -= latte_ingredients.get('water')
            resources.update({'water': water})
            milk -= latte_ingredients.get('milk')
            resources.update({'milk': milk})
            coffee -= espresso_ingredients.get('coffee')
            resources.update({'coffee': coffee})
            # water = 40
            # resources.update({'water': water})
            # coffee = 25
            # resources.update({'coffee': coffee})
            # print(water, coffee)

            #enough_resources = False
    elif order == "cappuccino":
        if (cappuccino_ingredients.get('water') > water
                and cappuccino_ingredients.get('milk') > milk
                and cappuccino_ingredients.get('coffee') > coffee
        ):
            print("Sorry, there is not enough water or coffee.\n")
            enough_resources = False
        elif cappuccino_ingredients.get('water') > water:
            print("Sorry, there is not enough water.\n")
            enough_resources = False
        elif cappuccino_ingredients.get('milk') > water:
            print("Sorry, there is not enough milk.\n")
            enough_resources = False
        elif cappuccino_ingredients.get('coffee') > coffee:
            print("Sorry, there is not enough coffee.\n")
            enough_resources = False
        else:
            # if (espresso_ingredients.get('water') <= water and espresso_ingredients.get('coffee') <= coffee):
            water -= cappuccino_ingredients.get('water')
            resources.update({'water': water})
            milk -= cappuccino_ingredients.get('milk')
            resources.update({'milk': milk})
            coffee -= cappuccino_ingredients.get('coffee')
            resources.update({'coffee': coffee})
            # water = 40
            # resources.update({'water': water})
            # coffee = 25
            # resources.update({'coffee': coffee})
            # print(water, coffee)
            # enough_resources = False

    # global resources
    # for key, value in resources:
    #     print(f"{key}: {value}")
    # print(resources)

def check_money(money, cost, order):
    global profit
    if cost > money:
        # not_enough_money = False
        print("\nSorry, that's not enough. Money refunded.")
        refill()
        # return not_enough_money
    elif cost < money:
        change = money - cost
        profit += money - change
        print(f"\nYou have ${round(change, 2)} in change. Here is your {order}. Enjoy!")
        # print("\nHere is your espresso. Enjoy!")
        # print(f"${profit}")
    elif cost == money:
        profit += money
        print(f"\nHere is your {order}. Enjoy!")
        # print(f"${profit}")

    # print(money)
    # print(cost)
    # print(f"${profit}")


def insert_coins():
    coins = 0.00
    add_more_coins = True
    while add_more_coins:
        add_coins = input(f"""
        ${round(coins, 2)}   (Q)uarters
               (D)imes
               (N)ickels
               (P)ennies\n
               (F)inished\n
        Insert coin: """).lower()
        if add_coins == "q":
            coins += 0.25
        elif add_coins == "d":
            coins += 0.10
        elif add_coins == "n":
            coins += 0.05
        elif add_coins == "p":
            coins += 0.01
        if add_coins == "f":
            add_more_coins = False
    return coins

# def shutdown():
#     return


def use_machine():
    while coffee_machine_on:
        print("\n===COFFEE TSUNAMI 2000===\n")
        user_selection()
    # print(coffee_machine_on)

use_machine()