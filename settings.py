from random import randint


class Player:
    def __init__(self, name, money, heat, intel, inventory):
        self.name = name
        self.money = money
        self.heat = heat
        self.intel = intel
        self.inventory = inventory

    def rob_a_store(self):
        heat_change = randint(1, 10)
        stolen_money = randint(0, 150)

        self.heat += heat_change
        self.money += stolen_money

        print("You robbed a store...")
        print("You attracted {} heat.".format(self.heat))

        if stolen_money > 0:
            print("You got {} credits.".format(stolen_money))
        else:
            print("But you got nothing.")

    def lay_low(self):
        heat_change = 5
        if (self.heat - heat_change) <= 0:
            self.heat = 0
        else:
            self.heat -= heat_change

        if self.heat > 0:
            print("You lay low for a week. You lost some heat.")

        else:
            print("You chill with some friends for a week.")

    def gain_intel(self):
        intel_gain = randint(1, 20)
        heat_change = randint(1, 15)

        self.heat += heat_change
        self.intel += intel_gain

        print("You attracted {} heat.".format(heat_change))
        print("Also, you gained {} intel.".format(intel_gain))

    def attack_server_farm(self, server_farm):
        server_farm.server_security += (self.heat / 2)

        if (server_farm.server_security - self.intel) <= 50:

            stolen_money = randint(800, 5000)
            heat_change = randint(1, 15)

            self.heat += heat_change
            self.money += stolen_money

            self.intel = 0

            print("You got around all security.")
            print("The stolen data was sold for {} credits.".format(stolen_money))
            print("Also, the corp put out a warrant for you. Gain {} heat.".format(heat_change))

        else:

            stolen_money = randint(100, 800)
            heat_change = randint(10, 25)

            self.heat += heat_change
            self.money += stolen_money

            self.intel = 0

            print("You barely got out of there.")
            print("Scraps of data you collected were sold on black market for {} credits.".format(stolen_money))
            print("Corp is breathing down your neck. Gain {} heat.".format(heat_change))

    def go_shopping(self, store):
        print("1. Pay {} credits for {} intel".format(store.intel_price, store.intel_amount))
        print("2. Leave shop")

        try:
            game_choice = int(input("Enter your choice [1-2]:"))
            if self.money < store.intel_price:
                print("You don't have enough money to buy anything.")
                game_choice = 2

            if game_choice == 1:

                self.money -= store.intel_price
                self.intel += store.intel_amount

                print("The girl behind the counter sells you some juicy intel.")

            elif game_choice == 2:
                print("You leave without buying anything.")

        except ValueError:
            print("Only use numbers")


class ServerFarm:
    def __init__(self, server_security):
        self.server_security = server_security


class Store:
    def __init__(self, intel_price, intel_amount):
        self.intel_price = intel_price
        self.intel_amount = intel_amount
