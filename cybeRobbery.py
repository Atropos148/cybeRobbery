#! python3
# cybeRobbery - game about robbing corps blind
# made by @atropos148

from settings import *

from random import randint
import time
import os
import sys


def main_menu():
    os.system("clear")
    print(15 * "-", " Menu ", 15 * "-")
    print("1. Play Game")
    print("2. Option 2")
    print("3. Exit")
    print(38 * "-")


def main_game():
    # TODO: ADD INVENTORY, GEAR, MERCS

    game_money = money
    game_heat = heat
    game_intel = intel

    game_server_security = server_security

    game_intel_price = intel_price
    game_intel_store = intel_store

    game_loop = True
    while game_loop:

        if game_heat > 100:
            print("You attracted too much heat. AugCops kicked down your door. Have fun in prison!")
            game_loop = False

        input("Press Enter")

        os.system("clear")
        print(42 * "-")
        print("- {} credits ----- {} heat ----- {} intel -".format(game_money, game_heat, game_intel))
        # print("- {} -".format(time.asctime(time.localtime(time.time()))))
        print("1. Rob a store")
        print("2. Lay low")
        print("3. Gain intel")
        print("4. Attack server farm")
        print("5. Store")

        print("7. Exit")
        print(42 * "-")

        try:
            game_choice = int(input("Enter your choice [1-2]:"))

            # ROB A STORE
            if game_choice == 1:
                stolen_money = randint(-50, 150)
                heat_change = randint(1, 10)

                game_heat += heat_change
                game_money += stolen_money

                print("You attracted {} heat.".format(game_heat))
                print("You robbed a store...")
                if stolen_money > 0:
                    print("You got {} credits.".format(stolen_money))
                elif stolen_money < 0:
                    print("You lost {} credits.".format(stolen_money))
                else:
                    print("But you got nothing.")

            # LAY LOW
            elif game_choice == 2:
                heat_change = 5
                if (game_heat - heat_change) <= 0:
                    game_heat = 0
                else:
                    game_heat -= heat_change

                if game_heat > 0:
                    print("You lay low for a week. You lost some heat")

                else:
                    print("You chill with some friends for a week.")

            # GAIN INTEL
            elif game_choice == 3:
                intel_gain = randint(1, 20)
                heat_change = randint(1, 15)

                game_heat += heat_change
                game_intel += intel_gain

                print("You attracted {} heat.".format(game_heat))
                print("Also, you gained {} intel.".format(intel_gain))

            # ATTACK SERVER FARM
            elif game_choice == 4:
                game_server_security += (game_heat/2)

                if (game_server_security - game_intel) <= 50:

                    stolen_money = randint(800, 5000)
                    heat_change = randint(1, 10)

                    game_heat += heat_change
                    game_money += stolen_money

                    game_intel = 0

                    print("You got around all security.")
                    print("The stolen data was sold for {} credits.".format(stolen_money))
                    print("Also, the corp put out a warrant for you. Gain {} heat.".format(heat_change))

                else:

                    stolen_money = randint(100, 800)
                    heat_change = randint(10, 25)

                    game_heat += heat_change
                    game_money += stolen_money

                    game_intel = 0

                    print("You barely got out of there.")
                    print("Scraps of data you collected were sold on black market for {} credits.".format(stolen_money))
                    print("Corp is breathing down your neck. Gain {} heat.".format(heat_change))

            # STORE
            elif game_choice == 5:

                print("1. Pay {} credits for {} intel".format(game_intel_price, game_intel_store))
                print("2. Leave shop")

                try:
                    game_choice = int(input("Enter your choice [1-2]:"))

                    if game_choice == 1:
                        game_money -= game_intel_price
                        game_intel += game_intel_store

                        print("The girl behind the counter sell you some juicy intel.")

                    elif game_choice == 2:
                        print("You leave without buying anything.")

                except ValueError:
                    print("Only use numbers")

            # EXIT
            elif game_choice == 7:
                game_loop = False

            else:
                raise ValueError("Only type numbers")

        except ValueError:
            print("Only use numbers")


loop = True
while loop:
    main_menu()

    try:
        choice = int(input("Enter your choice [1-3]: "))

        if choice == 1:
            main_game()
        elif choice == 2:
            print("Chosen 2\n")
        elif choice == 3:
            print("Exit\n")
            loop = False
        else:
            raise ValueError("Only type numbers to choose\nPress any key to try again\n")

    except ValueError:
        print("Only type numbers [1-3] to choose\n")
