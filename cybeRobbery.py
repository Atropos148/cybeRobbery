#! python3
# cybeRobbery - game about robbing corps blind
# made by @atropos148

from settings import *
import tkinter as tk


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

    intel_store = Store(
        items_dict_start={'intel_big': {'name': 'Intel', 'amount': 30, 'price': 500},
                          },
        type_of_store='intel'
    )

    weapon_store = Store(
        items_dict_start={'pistol': {'name': 'Glock 17', 'amount': 1, 'attack': 3, 'price': 200},
                          'shotgun': {'name': 'Remington 870', 'amount': 1, 'attack': 6, 'price': 450}
                          },
        type_of_store='weapon'
    )

    return [player, server_farm, intel_store, weapon_store]


def show_choices(player):
    print(38 * "-")
    print("- {} credits --- {} heat --- {} intel -".format(player.money, player.heat, player.intel))
    print('Inventory:', end='')
    for item in player.inventory:
        # print(player.inventory[item]['amount'], end='')
        if player.inventory[item]['amount'] > 1:
            print(' {}'.format(item['amount']), item + ',', end='')
        else:
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


'''
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
'''


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

        # input("Continue...")

        show_choices(player)

        try:
            game_choice = int(input("Enter your choice [1-7]:"))

            # ROB A STORE
            if game_choice == 1:
                player.rob_a_store()

            # LAY LOW
            elif game_choice == 2:
                # TODO: Write dynamic store_list
                # store_list = [weapon_store, intel_store]
                player.lay_low()

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
            print("Only use numbers")


def main():
    main_game(setup())


def main_menu_tk():
    # TKinter
    main_menu = tk.Tk()
    main_menu.geometry('400x400')

    menu_top = 15 * "-", " Menu ", 15 * "-"
    menu_play = "1. Play Game"
    menu_options = "2. Options"
    menu_exit = "3. Exit"

    window = tk.Label(text="cyberRobbery")
    window.grid(column=1, row=0)
    window = tk.Label(text=menu_top)
    window.grid(column=1, row=1)

    # PLAY
    button = tk.Button(
        main_menu,
        text=menu_play,
        command=lambda: main_game_tk(main_menu))
    button.grid(column=1, row=2)

    # OPTIONS
    button = tk.Button(
        main_menu,
        text=menu_options)
    button.grid(column=1, row=3)

    # EXIT
    button = tk.Button(
        main_menu,
        text=menu_exit,
        command=quit)
    button.grid(column=1, row=4)

    main_menu.mainloop()


def main_game_tk(window):
    setup_list = setup()
    player = setup_list[0]
    server_farm = setup_list[1]
    intel_store = setup_list[2]
    weapon_store = setup_list[3]

    if player.heat > 100:
        print("You attracted too much heat. AugCops kicked down your door. Have fun in prison!")
        quit()

    main_game_window = window
    main_game_window.geometry('400x400')

    rob_text = "Rob a store"
    lay_text = "Lay low"
    intel_text = "Gain intel"
    inv_text = "Inventory:"

    label = tk.Label(main_game_window, text=inv_text)
    label.grid(column=1, row=0)

    info_text = tk.StringVar()
    info_text.set("- {} credits --- {} heat --- {} intel -".format(player.money, player.heat, player.intel))

    info_label = tk.Label(main_game_window, textvariable=info_text)
    info_label.grid(column=1, row=1)

    rob_button = tk.Button(
        main_game_window,
        text=rob_text,
        command=player.rob_a_store)
    rob_button.grid(column=1, row=2)

    lay_button = tk.Button(
        main_game_window,
        text=lay_text,
        command=player.lay_low)
    lay_button.grid(column=1, row=3)

    intel_button = tk.Button(
        main_game_window,
        text=intel_text,
        command=player.gain_intel)
    intel_button.grid(column=1, row=4)

    main_game_window.mainloop()


if __name__ == "__main__":
    main_menu_tk()
    # main()

