#! python3
# cybeRobbery - game about robbing corps blind
# made by @atropos148

from settings import *


def setup():
    player = Player(
        # name will be chosen by player later
        name='Joe',
        money=200,
        heat=0,
        intel=1,
        inventory=[],
    )

    server_farm = ServerFarm(
        server_security=100,
    )

    store = Store(
        intel_price=500,
        intel_amount=30,
    )

    return [player, server_farm, store]


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
    # TODO: ADD INVENTORY, GEAR, MERCS
    # TODO: ADD Name Choice

    player = setup_list[0]
    server_farm = setup_list[1]
    store = setup_list[2]

    game_loop = True
    while game_loop:

        if player.heat > 100:
            print("You attracted too much heat. AugCops kicked down your door. Have fun in prison!")
            game_loop = False

        input("Continue...")

        print(42 * "-")
        print("- {} credits ----- {} heat ----- {} intel -".format(player.money, player.heat, player.intel))
        print("1. Rob a store")
        print("2. Lay low")
        print("3. Gain intel")
        print("4. Attack server farm")
        print("5. Store")
        print("6. Exit")
        print(42 * "-")

        try:
            game_choice = int(input("Enter your choice [1-2]:"))

            # ROB A STORE
            if game_choice == 1:
                player.rob_a_store()

            # LAY LOW
            elif game_choice == 2:
                player.lay_low()

            # GAIN INTEL
            elif game_choice == 3:
                player.gain_intel()

            # ATTACK SERVER FARM
            elif game_choice == 4:
                player.attack_server_farm(server_farm)

            # STORE
            elif game_choice == 5:
                player.go_shopping(store)

            # EXIT
            elif game_choice == 6:
                game_loop = False

            else:
                raise ValueError("Only type numbers")

        except ValueError:
            print("Only use numbers")


def main():
    main_menu()


if __name__ == "__main__":
    main()
