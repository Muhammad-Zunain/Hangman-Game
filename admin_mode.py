
def admin():
    import functions
    dict={}
    print('_' * 50, '\n           ADMINISTRATOR MODE', '\n', '_' * 50, sep='')

    with open("ID.txt") as f:                   #password and ID of admin is retrieved from ID.txt and it is then verified.
        admin_name, pwd = f.read().split(",")
    dict[admin_name] = pwd
    id = input("Enter ID:\n")

    # if ID is correct.
    if id in dict:
        password = input("Enter password:\n")

        #if password is correct.
        if password == dict.get(id):
            functions.clearscreen()     #previous outputs are cleared from the screen.

            while True:
                print('_' * 50, '\n           ADMINISTRATOR MODE', '\n', '_' * 50, sep="")

                # Available tools for admin are displayed.
                options = input('Enter desired option\n1.Reset Scores\n2.Add Word(s)\n3.Change ID and Password\n\n\n[b]:back\n')


                if options == '1':      # for clearing all the previous scores from the scores.txt file.
                    with open('scores.txt', 'w') as reset_scores:
                        input("Score has been reset !\n\n\nPress Enter to continue !")
                        functions.clearscreen()

                elif options == '2':        # if admin selects to add words to the word list.
                    functions.clearscreen()

                    with open('words.txt', 'a') as f:       # The file containing all the words is opened.

                        no_of_words = input('Enter the number of words you want to add: ')  # The admin is asked for the number of words he/she wants to add.

                        if no_of_words.isdigit():       # checks if the given output is correct.
                            for i in range(1, int(no_of_words) + 1):
                                word_ = input(f'Enter word no.{i} \n')
                                f.write(' ' + word_)
                            functions.clearscreen()
                        else:
                            print('Invalid no. of words entered.')

                elif options == '3':                     # if admin wants to change the login credentials to access admin tools.
                    functions.clearscreen()
                    admin = input("Enter new ID :\n      ")                             # asks for new ID
                    password_=input("Enter new Password:\n     ")                       # new password is asked
                    with open ("ID.txt","w") as f:                                      # new id and password are then written on a file.
                        f.write(admin + "," + password_  )
                    input("Process complete !\n\n\nPress Enter to go to menu !")
                    functions.clearscreen()

                elif options == 'b':                        # To go back to previous menu.
                    functions.clearscreen()
                    break
                else:
                    functions.clearscreen()                     # condition for in correct inputs.
                    print('invalid option entered')

        else:           # incase of wrong password
            input("Incorrect Password !\n\nPress Enter to continue.")
            functions.clearscreen()
    else:           # for incorrect id.
        input("Incorrect ID !\n\nPress Enter to continue.")
        functions.clearscreen()