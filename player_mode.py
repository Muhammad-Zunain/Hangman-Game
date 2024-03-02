
def player():
    import functions
    while True:

        print('_' * 50, '\n                     PLAYER MODE', '\n', '_' * 50, sep="")
        player_ = input("\n\n1.Login\n2.Create New Account\n3.Play as guest\n\n\n[b] Back\n\n")
        functions.clearscreen()
        if player_ == "1":                  #login
            IDs = {}
            # collecting all the usernames & passwords and then comparing the username to the one provided by user.
            with open("account.txt") as f:
                S = f.read().split(",")
                S = S[:-1]
                print(len(S), S)
                for i in range(0, len(S), 2):
                    IDs[S[i]] = S[i + 1]
                ID = input("Enter ID: ")
                if ID in S:
                    password = input("Enter password: ")
                    if password == IDs.get(ID):
                        functions.game()     # the game function is called to start the game.

                # conditions for incorrect password or ID
                    else:
                        print("Incorrect password !")
                        input("\n\n\nPress Enter to continue !")
                        functions.clearscreen()
                else:
                    print("Incorrect ID !")
                    input("\n\n\nPress Enter to continue !")
                    functions.clearscreen()

        # To create new account
        elif player_ == "2":
            with open("account.txt", "a+") as file:

                while True:     # Takes input for new username & checks whether the given username is unique or not and then asks password.
                    file.seek(0)
                    ID = input("Enter ID: ")

                    IDs = []
                    lis = file.read().split(',')
                    for i in range(0, len(lis), 2):
                        if i != '':
                            IDs.append(lis[i])

                    if ID in IDs:
                        print('The ID with this name already exists. Try another one.')
                    elif ID == '':
                        print('No ID provided.')

                    else:

                        password = input("Enter password: ")
                        file.write(f'{ID},{password},')
                        break
            functions.game()

        #if the player wants to play as guest.
        elif player_ == "3":
            functions.game()

        #if the user wants to return to previous menu.
        elif player_ == "b":
            functions.clearscreen()
            break
        else:
            input('Invalid input. Press any key to continue\n')
            functions.clearscreen()