#! python3
# cybeRobbery - game about robbing corps blind
# made by @atropos148

from settings import *


def setup():
    player = Player(
        # name will be chosen by player later
        name='Joe',
        money=650,
        heat=0,
        intel=1,
        inventory={},
    )

    server_farm = ServerFarm(100, 'Sweigart Consortium')

    intel_big = Intel('E-Mails', 400, 30)

    intel_dict_start = {0: intel_big}
    intel_store = IntelStore(intel_dict_start, player)

    glock = Weapon('Glock 17', 200, 3)
    shotgun = Weapon('Remington 870', 450, 6)
    go_back = Item('Go Back', 0)
    items_dict_start = {0: glock, 1: shotgun, 9: go_back}

    weapon_store = WeaponStore(items_dict_start, player)

    return [player, server_farm, intel_store, weapon_store]


def main_menu():
    game_loop = True

    main_menu_options = {
        "Play Game": main_game,
        "Options": print("Not Done"),
        "Exit": quit
    }

    main_menu_object = Menu(main_menu_options)

    while game_loop:
        main_menu_object.show_options()


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
        "Attack Server Farm": player.attack_server_farm,
        "Intel Store": intel_store.show_intel,
        "Weapon Store": weapon_store.show_weapons,
        "Exit": quit
    }

    main_game_menu = MainGameMenu(main_game_options, player)

    game_loop = True
    while game_loop:

        if player.heat > 100:
            print("You attracted too much heat. AugCops kicked down your door. Have fun in prison!")
            break

        input("Continue...")

        main_game_menu.refresh_info()
        main_game_menu.show_options()


def main():
    main_menu()


if __name__ == "__main__":
    main()
