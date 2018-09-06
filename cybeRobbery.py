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

    server_farm = ServerFarm(
        server_security=100,
    )

    intel_big = Intel('E-Mails', 400, 30)

    intel_store = Store(
        items_dict_start={0: intel_big},
        type_of_store='intel'
    )

    glock = Weapon('Glock 17', 200, 3)
    shotgun = Weapon('Remington 870', 450, 6)

    weapon_store = Store(
        items_dict_start={0: glock, 1: shotgun},
        type_of_store='weapon'
    )

    return [player, server_farm, intel_store, weapon_store]


def show_choices(player):
    print(38 * "-")
    print("- {} credits --- {} heat --- {} intel -".format(player.money, player.heat, player.intel))
    print('Inventory:', end='')
    for item in player.inventory:
        # print(player.inventory[item]['amount'], end='')
        ''''
        if player.inventory[item]['amount'] > 1:
            print(' {}'.format(item['amount']), item + ',', end='')
        else:
            print(' ', item + ',', end='')
        '''
        print(' ', item + ',', end='')

    print()
    print(38 * "-")
    print("1. Rob a store")
    print("2. Lay low")
    print("3. Gain intel")
    print("4. Attack server farm")
    print("5. Intel Store")
    print("6. Weapon Store")
    print("7. Exit")
    print(38 * "-")


def main_menu():
    loop = True
    while loop:
        print(15 * "-", " Menu ", 15 * "-")
        print("1. Play Game")
        print("2. Options")
        print("3. Exit")
        print(38 * "-")
        try:
            choice = int(input("Enter your choice [1-3]: "))

            if choice == 1:
                main_game(setup())
            elif choice == 2:
                print("Chosen 2\n")
            elif choice == 3:
                print("Exit\n")
                loop = False
            else:
                raise ValueError("Only type numbers to choose\nPress any key to try again\n")

        except ValueError:
            print("Only type numbers [1-3] to choose\n")


def main_game(setup_list):
    # TODO: ADD GEAR, MERCS
    # TODO: ADD Name Choice

    player = setup_list[0]
    server_farm = setup_list[1]
    intel_store = setup_list[2]
    weapon_store = setup_list[3]

    game_loop = True
    while game_loop:

        if player.heat > 100:
            print("You attracted too much heat. AugCops kicked down your door. Have fun in prison!")
            break

        input("Continue...")

        show_choices(player)

        try:
            game_choice = int(input("Enter your choice [1-7]:"))

            # ROB A STORE
            if game_choice == 1:
                player.rob_a_store()

            # LAY LOW
            elif game_choice == 2:
                # TODO: Write dynamic store_list
                store_list = [weapon_store, intel_store]
                player.lay_low(store_list)

            # GAIN INTEL
            elif game_choice == 3:
                player.gain_intel()

            # ATTACK SERVER FARM
            elif game_choice == 4:
                player.attack_server_farm(server_farm)

            # INTEL STORE
            elif game_choice == 5:
                player.go_shopping(intel_store)

            # WEAPON STORE
            elif game_choice == 6:
                player.go_shopping(weapon_store)

            # EXIT
            elif game_choice == 7:
                game_loop = False

            else:
                raise ValueError("Only type numbers")

        except ValueError:
            print("ValueError: Only use numbers")


def main():
    main_menu()


if __name__ == "__main__":
    main()
