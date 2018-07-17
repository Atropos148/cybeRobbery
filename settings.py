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

    def go_shopping(self, store):

        store_dict = store.build_id_dict()
        store.show_items(store_dict, store.items_dict)

        store.sell_items(store_dict, store.items_dict, self)


class ServerFarm:
    def __init__(self, server_security):
        self.server_security = server_security


class Store:
    def __init__(self, items_dict_start, type_of_store):
        self.items_dict_start = items_dict_start
        self.type_of_store = type_of_store
        self.items_dict = copy.deepcopy(items_dict_start)

    def build_id_dict(self):

        id_dict = {}
        id_dict.clear()
        for i, item in enumerate(self.items_dict, 1):
            id_dict[i] = item
        return id_dict

    @staticmethod
    def show_items(id_dict, items_dict):
        for item in id_dict:
            curr_item = items_dict[id_dict[item]]

            amount_check = curr_item['amount'] if curr_item['amount'] > 1 else 'a'
            print('{}. Buy {} {} for {}'.format(
                item, amount_check, curr_item['name'], curr_item['price']))

        print('9. Leave')

    def sell_items(self, id_dict, items_dict, player):
        choice = int(input('What do  you want to buy?(1-9) '))
        id_dict_check = []
        for item in id_dict:
            id_dict_check.append(item)

        try:
            if choice in id_dict_check:

                # in a list of all items in shop, choose the item player selected
                chosen_item = items_dict[id_dict[choice]]

                if player.money < int(chosen_item['price']):
                    print("You don't have enough money to buy {}".format(chosen_item['name']))

                else:
                    if self.type_of_store == 'intel':
                        player.money -= int(chosen_item['price'])
                        player.intel += int(chosen_item['amount'])
                        # print('You bought {}'.format(chosen_item['name']))

                    elif self.type_of_store == 'weapon':
                        player.money -= int(chosen_item['price'])

                        if chosen_item['name'] in player.inventory:
                            player.inventory[chosen_item['amount']] += 1

                        else:
                            player.inventory[chosen_item['name']] = chosen_item

                        # print('You bought {}'.format(chosen_item['name']))
                        del items_dict[id_dict[choice]]

                    print('You bought {}'.format(chosen_item['name']))

            else:
                print('Wrong numbesdadasdr')

        except KeyError:
            print(KeyError)
