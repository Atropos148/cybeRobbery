#! python3
# cybeRobbery - game about robbing corps blind
# made by @atropos148

import pygame

from settings import *

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

green_hover = (0, 200, 0)
red_hover = (200, 0, 0)

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
        inventory={}
    )

    server_farm = ServerFarm(100, 'Sweigart Consortium', player)
    intel_big = Intel('E-Mails', 400, 30)

    intel_dict_start = {0: intel_big}
    intel_store = IntelStore(intel_dict_start, player)

    glock = Weapon('Glock 17', 200, 3)
    shotgun = Weapon('Remington 870', 450, 6)
    go_back = Item('Go Back', 0)
    items_dict_start = {0: glock, 1: shotgun, 9: go_back}

    weapon_store = WeaponStore(items_dict_start, player)

    return [player, server_farm, intel_store, weapon_store]


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def button(msg, x, y, width, height, color_normal, color_hover, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(game_display, color_hover, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(game_display, color_normal, (x, y, width, height))

    color = black
    small_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rect = text_objects(msg, small_text, color)
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    game_display.blit(text_surface, text_rect)


def quit_game():
    pygame.quit()
    quit()


def main_menu():
    game_loop = True

    main_menu_options = {
        "Play Game": main_game,
        "Options": print("Not Done"),
        "Exit": quit_game
    }

    main_menu_object = Menu(main_menu_options)

    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        game_display.fill(black)

        large_text = pygame.font.Font('freesansbold.ttf', 64)
        text_surface, text_rect = text_objects("cybeRobbery", large_text, green)
        text_rect.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surface, text_rect)

        y = 50
        for option in main_menu_options:
            button(option, 50, y, 200, 50, green, green_hover, main_menu_options[option])
            y += 70

        pygame.display.update()
        clock.tick(60)

        # main_menu_object.show_options()


def main_game():
    # TODO: ADD GEAR, MERCS
    # TODO: ADD Name Choice

    setup_list = setup()

    player = setup_list[0]
    server_farm = setup_list[1]
    intel_store = setup_list[2]
    weapon_store = setup_list[3]

    main_game_options = {
        "Rob a store": player.rob_a_store,
        "Lay low": player.lay_low,
        "Gain Intel": player.gain_intel,
        "Attack Server Farm": server_farm.server_farm_assault,
        "Intel Store": intel_store.show_intel,
        "Weapon Store": weapon_store.show_weapons,
        "Exit": quit
    }

    main_game_menu = MainGameMenu(main_game_options, player)

    game_loop = True
    while game_loop:

        large_text = pygame.font.Font('freesansbold.ttf', 64)
        small_text = pygame.font.Font('freesansbold.ttf', 16)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        if player.heat > 100:
            ending_text = "You attracted too much heat. AugCops kicked down your door. Have fun in prison!"
            text_surface, text_rect = text_objects(ending_text, small_text, green)
            text_rect.center = ((display_width / 2), (display_height / 2))
            game_display.blit(text_surface, text_rect)
            break

        game_display.fill(black)

        info_text = main_game_menu.refresh_info_text()
        text_surface, text_rect = text_objects(info_text, small_text, green)
        text_rect.center = ((display_width / 2), 24)
        game_display.blit(text_surface, text_rect)

        y = 50
        for option in main_game_options:
            button(option, 50, y, 200, 50, green, green_hover, main_game_options[option])
            y += 70

        pygame.display.update()
        clock.tick(60)


def main():
    main_menu()


if __name__ == "__main__":
    main()
