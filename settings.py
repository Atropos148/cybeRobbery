from random import randint
import copy


class Player:
    def __init__(self, name, money, heat, intel, inventory):
        self.name = name
        self.money = money
        self.heat = heat
        self.intel = intel
        self.inventory = inventory

    @staticmethod
    def restock_stores(store_list):
        for store in store_list:
            store.items_dict.clear()
            store.items_dict = copy.deepcopy(store.items_dict_start)

    def rob_a_store(self):
        heat_change = randint(1, 10)
        stolen_money = randint(0, 150)

        self.heat += heat_change
        self.money += stolen_money

        print("You robbed a store...")

        heat_change_check = heat_change if heat_change > 0 else 'no'
        print("You attracted {} heat.".format(heat_change_check))

        stolen_money_check = stolen_money if stolen_money > 0 else 'no'
        print("You got {} credits.".format(stolen_money_check))

    def lay_low(self, store_list):
        self.restock_stores(store_list)

        heat_change = randint(3, 15)

        if (self.heat - heat_change) <= 0:
            self.heat = 0
        else:
            self.heat -= heat_change

        heat_change_effect_check = \
            'You lay low for a week. You lost some heat.' if self.heat > 0 \
            else 'You chill with some friends for a week.'

        print(heat_change_effect_check)

    def gain_intel(self):
        intel_gain = randint(1, 20)
        heat_change = randint(1, 15)

        self.heat += heat_change
        self.intel += intel_gain

        print('You spent the week spying on the server farm both in real life and in cyber.')

        heat_change_check = heat_change if heat_change > 0 else 'no'
        print("You attracted {} heat.".format(heat_change_check))

        intel_change_check = intel_gain if intel_gain > 0 else 'no'
        print("Also, you gained {} intel.".format(intel_change_check))

    def attack_server_farm(self, server_farm):
        server_farm.server_security += (self.heat / 2)
        print(server_farm.name)
        # if the attack is successful
        # TODO: Add READY LEVEL
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

            stolen_money = randint(100, 600)
            heat_change = randint(10, 25)

            self.heat += heat_change
            self.money += stolen_money

            self.intel = 0

            print("You barely got out of there.")
            print("Scraps of data you collected were sold on black market for {} credits.".format(stolen_money))
            print("Corp is breathing down your neck. Gain {} heat.".format(heat_change))


class ServerFarm:
    def __init__(self, server_security, name):
        self.server_security = server_security
        self.name = name


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getname(self):
        return self.name


class Weapon(Item):
    def __init__(self, name, price, attack):
        Item.__init__(self, name, price)
        self.attack = attack

    def getname(self):
        return self.name


class Intel(Item):
    def __init__(self, name, price, intel_amount):
        Item.__init__(self, name, price)
        self.intel_amount = intel_amount


class Menu:
    def __init__(self, options):
        self.options = options

    def choose_option(self, options_dict):
        try:
            choice = int(input("Enter your choice: "))
            if choice in options_dict:
                options_dict[choice]()
            else:
                raise ValueError("Only type numbers to choose")

        except ValueError:
            print("Invalid number, please choose again")

    def show_options(self):
        index_dict = {}
        print(15 * "-", " Menu ", 15 * "-")
        for index, option in enumerate(self.options):
            connected_function = self.options[option]

            print(str(index + 1) + ". " + str(option))
            index_dict[index + 1] = connected_function

        print(38 * "-")
        self.choose_option(index_dict)


class MainGameMenu(Menu):
    def __init__(self, options, player):
        Menu.__init__(self, options)
        self.player = player

    def refresh_info(self):
        print(38 * "-")
        print("- {} credits --- {} heat --- {} intel -".format(self.player.money, self.player.heat, self.player.intel))
        print('Inventory: ', end='')
        for item in self.player.inventory:
            print(str(self.player.inventory[item].name) + ', ', end='')
        print('\n')

    def show_options(self):
        index_dict = {}

        for index, option in enumerate(self.options):
            connected_function = self.options[option]

            print(str(index + 1) + ". " + option)
            index_dict[index + 1] = connected_function

        print(38 * "-")
        self.choose_option(index_dict)


class WeaponStore(Menu):
    def __init__(self, items_dict_start, player):
        items_dict = items_dict_start
        self.options = items_dict
        Menu.__init__(self, self.options)
        self.player = player

    def choose_weapon(self, options_dict, player):
        try:

            choice = int(input("What are you buying?: "))
            chosen_gun = options_dict[choice]
            if choice in options_dict:
                if player.money >= chosen_gun.price:
                    player.money -= int(chosen_gun.price)
                    player.inventory[chosen_gun.name] = chosen_gun
                else:
                    print("You don't have enough money to buy " + chosen_gun.name + "!")

            else:
                raise ValueError("Only type numbers to choose")

        except ValueError:
            print("Invalid number, please choose again")

    def show_weapons(self):
        index_dict = {}
        print(15 * "-", " Menu ", 15 * "-")
        for index, option in enumerate(self.options):
            connected_gun = self.options[option]

            print(str(index + 1) + ". " + str(self.options[option].name))
            index_dict[index + 1] = connected_gun

        print(38 * "-")
        self.choose_weapon(index_dict, self.player)


class IntelStore(Menu):
    def __init__(self, items_dict_start, player):
        items_dict = items_dict_start
        self.options = items_dict
        Menu.__init__(self, self.options)
        self.player = player

    def choose_intel(self, options_dict, player):
        try:

            choice = int(input("What are you buying?: "))
            chosen_intel = options_dict[choice]
            if choice in options_dict:
                if player.money >= chosen_intel.price:
                    player.money -= chosen_intel.price
                    player.intel += chosen_intel.intel_amount

            else:
                raise ValueError("Only type numbers to choose")

        except ValueError:
            print("Invalid number, please choose again")

    def show_intel(self):
        index_dict = {}
        print(15 * "-", " Menu ", 15 * "-")
        for index, option in enumerate(self.options):
            connected_intel = self.options[option]

            print(str(index + 1) + ". " + str(self.options[option].name))
            index_dict[index + 1] = connected_intel

        print(38 * "-")
        self.choose_intel(index_dict, self.player)
