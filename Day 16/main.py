from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# menuitem = MenuItem(name='name', cost='cost', water='water', milk='milk', coffee='coffee')
# menuitem = MenuItem('name', 'water', 'milk', 'coffee', 'cost')
menuitem = MenuItem(name='name', water='water', milk='milk', coffee='coffee', cost='cost')
coffeemaker = CoffeeMaker()
money = MoneyMachine()
power = True
options = menu.get_items()


while power:
    print("\n===== Coffee Tsunami 2000 =====\n")
    selection = input(f"What would you like? ({options}): ").lower()
    drink = menu.find_drink(selection)
    # order_cost = menu.menu[0]
    # print(order_cost)

    # Shutdown the machine
    if selection == "off":
        print("Powering off. Goodbye.")
        power = False

    # Print report
    elif selection == "report":
        # print("\n")
        coffeemaker.report()
        money.report()

    # Are resources sufficient
    # elif selection == menuitem('name'):
    #     print("yes")

    # elif selection == "latte":
    elif drink:
        # print(selection)
        # print(menu.find_drink(order_name=selection))
        # print(coffeemaker.is_resource_sufficient(menu.find_drink(selection)))
        if coffeemaker.is_resource_sufficient(drink):
            # print("yes")
            # cost = money.process_coins()
            # print(cost)
            # print(menuitem.cost('cost'))
            # print(menu.menu('cost'))
            # print(cost)
            # print(money.make_payment(cost=menu.menu('cost')))
            # print(money.process_coins())

            if money.make_payment(cost=drink.cost):
                 coffeemaker.make_coffee(drink)

        # if coffeemaker.is_resource_sufficient(menuitem):
        #     # print(selection.name)
        #          print("yes")

        # print("yes")
        # #
        #     selection == "latte"):
        #
        # if menu.find_drink(order_name=selection):
        #     menu.get_items()

    # else:
    #     menu.find_drink(selection)


    # if selection == "latte":
    #     if menu.find_drink('name'):
    #         print('name')
    #     else:
    #         print(type)
    # elif selection == "espresso":
    #     print(type)
    # elif selection == "cappuccino":
    #     menu.get_items()
    # else:





