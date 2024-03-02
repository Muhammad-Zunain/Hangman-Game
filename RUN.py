import functions
import admin_mode
import player_mode
input("""
              *************************************************************************
              | |       |   ______             ______    _       _   ______  |\     | |
              | |       |  |      |  |\    |  |      |  | \     / | |      | | \    | |
              | |-------|  |______|  | \   |  |         |  \   /  | |______| |  \   | |
              | |       |  |      |  |  \  |  |     _   |   \_/   | |      | |   \  | |
              | |       |  |      |  |   \_|   \____/   |         | |      | |    \_| |
              *************************************************************************


                                                         +--------+
                                                               | \|
                                                             o_|  |
                                                            /|\   | 
                      _ _ _ _ _ _ _ _                        |    |
                  press Enter to continue!!                 / \   |
                                                        ===========""")
functions.clearscreen()         # clears previous outputs from the screen. Defined in "functions.py".
while True:
    mode = input(f'\n\n{"-" * 20}SELECT MODE{"-" * 20}\n\n1.ADMINISTRATOR MODE\n2.PLAYER MODE\n\n\n[q]:quit\n\n')
    functions.clearscreen()

    if mode == '1':
        admin_mode.admin()          # opens administrator mode defined in "admin_mode.py"

    elif mode == '2':
       player_mode.player()         # opens player mode defined in "player_mode.py"
    elif mode == 'q':
        break                       # for exiting the game.
    else:
        input('Invalid input. Press any key to continue\n')         # error message for incorrect inputs.
        functions.clearscreen()
