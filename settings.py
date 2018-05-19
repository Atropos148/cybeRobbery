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

        shopping_result = store.sell_items(store.show_items(), self.money, self.intel)
        self.money = shopping_result[0]
        self.intel = shopping_result[1]


class ServerFarm:
    def __init__(self, server_security):
        self.server_security = server_security


class Store:
    def __init__(self, items_dict):
        self.items_dict = items_dict

    def show_items(self):
        i = 0
        id_dict = {}
        for item in self.items_dict:
            i += 1
            curr_item = self.items_dict[item]
            id_dict[i] = item
            print('{}. Buy {} {} for {}'.format(
                i, curr_item['amount'], curr_item['name'], curr_item['price']))

        return id_dict

    def sell_items(self, id_dict, player_money, player_intel):
        choice = int(input('What do  you want to buy?(1) '))
        item = id_dict[choice]
        if player_money < int(self.items_dict[item]['price']):
            print('You dont have enough money to buy {}'.format(self.items_dict[item]['name']))
        else:
            player_money -= int(self.items_dict[item]['price'])
            player_intel += int(self.items_dict[item]['amount'])
            print('You bought {}'.format(self.items_dict[item]['name']))

        return player_money, player_intel
