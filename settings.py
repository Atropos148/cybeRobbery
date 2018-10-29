from random import randint
import copy
import pygame
import types

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

        # TODO: Add visual feedback with info

        # print("You robbed a store...")

        heat_change_check = heat_change if heat_change > 0 else 'no'
        # print("You attracted {} heat.".format(heat_change_check))

        stolen_money_check = stolen_money if stolen_money > 0 else 'no'
        # print("You got {} credits.".format(stolen_money_check))

        return heat_change_check, stolen_money_check

    def lay_low(self):
        # self.restock_stores(store_list)

        heat_change = randint(3, 15)

        if (self.heat - heat_change) <= 0:
            self.heat = 0
        else:
            self.heat -= heat_change

        '''
        heat_change_effect_check = \
            'You lay low for a week. You lost some heat.' if self.heat > 0 \
            else 'You chill with some friends for a week.'
        
        print(heat_change_effect_check)
        '''

    def gain_intel(self):
        intel_gain = randint(1, 20)
        heat_change = randint(1, 15)

        self.heat += heat_change
        self.intel += intel_gain

        # print('You spent the week spying on the server farm both in real life and in cyber.')

        # heat_change_check = heat_change if heat_change > 0 else 'no'
        # print("You attracted {} heat.".format(heat_change_check))

        # intel_change_check = intel_gain if intel_gain > 0 else 'no'
        # print("Also, you gained {} intel.".format(intel_change_check))

    def refresh_info_text(self):
        return ("- Name: {} --- Credits: {} --- Heat: {} --- Intel:{} -".format(
            self.name, self.money, self.heat, self.intel))


class ServerFarm:
    def __init__(self, server_security, name, player):
        self.server_security = server_security
        self.name = name
        self.player = player

    def server_farm_assault(self):
        self.server_security += (self.player.heat / 2)
        # print(self.name)
        # if the attack is successful
        # TODO: Add READY LEVEL
        if (self.server_security - self.player.intel) <= 50:

            stolen_money = randint(800, 5000)
            heat_change = randint(1, 15)

            self.player.heat += heat_change
            self.player.money += stolen_money

            self.player.intel = 0

            print("You got around all security.")
            print("The stolen data was sold for {} credits.".format(stolen_money))
            print("Also, the corp put out a warrant for you. Gain {} heat.".format(heat_change))

        else:

            stolen_money = randint(100, 600)
            heat_change = randint(10, 25)

            self.player.heat += heat_change
            self.player.money += stolen_money

            self.player.intel = 0

            print("You barely got out of there.")
            print("Scraps of data you collected were sold on black market for {} credits.".format(stolen_money))
            print("Corp is breathing down your neck. Gain {} heat.".format(heat_change))


class Item:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def getname(self):
        return self.name


class Weapon(Item):
    def __init__(self, name, price, attack, description):
        Item.__init__(self, name, price, description)
        self.attack = attack

    def getname(self):
        return self.name


class Intel(Item):
    def __init__(self, name, price, intel_amount, description):
        Item.__init__(self, name, price, description)
        self.intel_amount = intel_amount


class Menu:
    def __init__(self, options):
        self.options = options
        self.display_width = 800
        self.display_height = 600

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

        self.green_hover = (0, 200, 0)
        self.red_hover = (200, 0, 0)

        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))

    @staticmethod
    def text_objects(text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def button(self, msg, x, y, width, height, color_normal, color_hover, action, description, click):
        mouse = pygame.mouse.get_pos()
        # click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.game_display, self.green, (x - 5, y - 5, width + 10, height + 10))
            pygame.draw.rect(self.game_display, color_hover, (x, y, width, height))

            color = self.green
            small_text = pygame.font.Font('freesansbold.ttf', 20)
            text_surface, text_rect = self.text_objects(description, small_text, color)
            text_rect.center = (self.display_width / 2, self.display_height - 30)
            self.game_display.blit(text_surface, text_rect)

            if click is True and action is not None:
                if type(action) is tuple:
                    action[0](action[1])
                else:
                    action()

        else:
            pygame.draw.rect(self.game_display, color_normal, (x, y, width, height))

        color = self.green
        small_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surface, text_rect = self.text_objects(msg, small_text, color)
        text_rect.center = ((x + (width / 2)), (y + (height / 2)))
        self.game_display.blit(text_surface, text_rect)

    def show_menu_options(self, click_state):
        y = 50
        for option in self.options:
            # option[0] is first letter of key in the options dictionary, key is a string
            action = self.options[option][0]
            description = self.options[option][1]
            self.button(option, 50, y, 200, 50, self.black, self.black, action, description, click_state)
            y += 70

    def show_menu_name(self):
        self.game_display.fill(self.black)

        large_text = pygame.font.Font('freesansbold.ttf', 64)
        text_surface, text_rect = self.text_objects("cybeRobbery", large_text, self.black)
        text_rect.center = ((self.display_width / 2), (self.display_height / 2))
        self.game_display.blit(text_surface, text_rect)


class MainGameMenu(Menu):
    def __init__(self, options):
        Menu.__init__(self, options)


class WeaponStore(Menu):
    def __init__(self, items_dict_start, player):
        items_dict = items_dict_start
        self.options = items_dict
        Menu.__init__(self, self.options)
        self.player = player

    def show_weapons(self, click_state):
        y = 50
        for weapon in self.options:
            weapon = self.options[weapon]
            print(weapon.description)
            self.button(weapon.name, 300, y, 200, 50, self.black, self.black, "test2", weapon.description, click_state)
            y += 70

class IntelStore(Menu):
    def __init__(self, items_dict_start, player):
        items_dict = items_dict_start
        self.options = items_dict
        Menu.__init__(self, self.options)
        self.player = player
