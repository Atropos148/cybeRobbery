#! python3
# cybeRobbery - game about robbing corps blind
# made by @atropos148

# import pygame
import time

from settings import *

resolutions_list = ((800, 600), (1280, 720), (1920, 1080))

_1080p = resolutions_list[2]
_720p = resolutions_list[1]
_800x600 = resolutions_list[0]

display_width = _720p[0]
display_height = _720p[1]

resolution = (display_width, display_height)

black = (0, 0, 0)
green = (0, 255, 0)
'''
white = (255, 255, 255)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

green_hover = (0, 200, 0)
red_hover = (200, 0, 0)
'''

pygame.init()
clock = pygame.time.Clock()

game_display = pygame.display.set_mode((display_width, display_height))


def setup():
    player = Player(
        # name will be chosen by player later
        name='Joe',
        money=650,
        heat=0,
        intel=1,
        inventory=[]
    )

    server_farm = ServerFarm(100, 'Sweigart Consortium', player)
    intel_big = Intel('E-Mails', 400, 30, "Bunch of internal emails with passwords")

    intel_dict_start = {0: intel_big}
    intel_store = IntelStore(intel_dict_start, player, False, resolution)

    glock = Weapon('Glock 17', 200, 3, "Small Handgun")
    shotgun = Weapon('Remington 870', 450, 6, "Kill everyone with this")
    # go_back = Item('Go Back', 0, "Return")
    items_dict_start = {0: glock, 1: shotgun}

    weapon_store = WeaponStore(items_dict_start, player, False, resolution)

    return player, server_farm, intel_store, weapon_store


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def quit_game():
    pygame.quit()
    quit()


def main_menu():
    game_loop = True

    main_menu_options = {
        "Play Game": [main_game, 'Start the game'],
        # "Options": print("Not Done"),
        "Exit": [quit_game, 'Quit the game']
    }

    main_menu_object = Menu(main_menu_options, resolution)

    click = False
    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONUP:
                click = True

        '''
        large_text = pygame.font.Font('freesansbold.ttf', 64)
        text_surface, text_rect = text_objects("cybeRobbery", large_text, black)
        text_rect.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surface, text_rect)
        '''

        main_menu_object.show_menu_name()
        main_menu_object.show_menu_options(click)

        pygame.display.update()
        clock.tick(60)


def main_game():
    # TODO: ADD GEAR, MERCS
    # TODO: ADD Name Choice

    player, server_farm, intel_store, weapon_store = setup()

    player.change_name("Change Me")

    # Tuples can pass arguments in this bit of code
    # weapon_store_object = (weapon_store.open_store, False)

    main_game_options = {
        "Rob a store": [player.rob_a_store, 'Knock over a store to get Money'],
        "Lay low": [player.lay_low, 'Get rid of Heat by not doing much'],
        "Gain Intel": [player.gain_intel, 'Spend time by spying in real and cyber'],
        "Attack Server Farm": [server_farm.server_farm_assault, 'Launch an Assault'],
        "Intel Store": [intel_store.open_store, 'Buy some info on your enemies'],
        "Weapon Store": [weapon_store.open_store, 'Get some guns off the books'],
        "Exit": [main_menu, 'Quit the game']
    }

    main_game_menu = MainGameMenu(main_game_options, resolution)

    game_loop = True

    while game_loop:

        # large_text = pygame.font.Font('freesansbold.ttf', 64)
        small_text = pygame.font.Font('freesansbold.ttf', 16)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONUP:
                click = True

        # GAME OVER check
        if player.heat > 100:
            end_game_options = {
                "Main Menu": [main_menu, 'Go back to Menu'],
            }

            game_display.fill(black)

            end_game_menu = Menu(end_game_options, resolution)
            end_game_menu.show_menu_options(click)

            game_display.fill(black)

            ending_text = "You attracted too much heat. AugCops kicked down your door. Have fun in prison!"
            text_surface, text_rect = text_objects(ending_text, small_text, green)
            text_rect.center = ((display_width / 2), (display_height / 2))
            game_display.blit(text_surface, text_rect)
            pygame.display.update()
            time.sleep(1)
            main_menu()

        game_display.fill(black)

        info_text_main = player.refresh_info_text()[0]
        info_text_inventory = player.refresh_info_text()[1]

        # Money and Heat, x:400, y: 25 > 800x600
        text_surface, text_rect = text_objects(info_text_main, small_text, green)
        text_rect.center = ((display_width / 2), ((display_height / 100) * 4))
        game_display.blit(text_surface, text_rect)

        # Inventory x:400, y: 45 > 800x600
        text_surface, text_rect = text_objects(info_text_inventory, small_text, green)
        text_rect.center = ((display_width / 2), ((display_height / 100) * 7))
        game_display.blit(text_surface, text_rect)

        if weapon_store.store_open is True:
            weapon_store.show_weapons(click)
        if intel_store.store_open is True:
            intel_store.show_intel(click)

        main_game_menu.show_menu_options(click)

        pygame.display.update()
        clock.tick(60)


def main():
    main_menu()


if __name__ == "__main__":
    main()
