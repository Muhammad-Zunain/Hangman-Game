def hangman (guess):          # Function for displaying hangman incase of deduction of guesses.
    if guess == 5:
        print("+--------+")
        print("        \|")
        print("         |")
        print("         |")
        print("   / \   |")
        print("==========")
    elif guess == 4:
        print("+--------+")
        print("        \|")
        print("         |")
        print("    |    |")
        print("   / \   |")
        print("==========")
    elif guess == 3:
        print("+--------+")
        print("        \|")
        print("    |    |")
        print("    |    |")
        print("   / \   |")
        print("==========")
    elif guess == 2:
        print("+--------+")
        print("        \|")
        print("         |")
        print("   /|\   |")
        print("    |    |")
        print("   / \   |")
        print("==========")
    elif guess == 1:
        print("+--------+")
        print("        \|")
        print("    o_|  |")
        print("   /|\   |")
        print("    |    |")
        print("   / \   |")
        print("==========")
    elif guess == 0:
        print("+--------+")
        print("      | \|")
        print("    o_|  |")
        print("   /|\   |")
        print("    |    |")
        print("   / \   |")
        print(" =========")


# Function for clearing the previous outputs from the screen.
def clearscreen():
    import os
    os.system('cls')


# Function containing the main game program.
def game():
    import random
    while True:
        clearscreen()
        print('_' * 50, '\n                     PLAYER MODE', '\n', '_' * 50, sep="")
        player_options = input('\n\n\n1. Play game.\n2. Display score.\n3. Rules\n\n[b] back\n\n')
        while True:
            clearscreen()

            # To play game.
            if player_options == '1':

                username = input('\n\n\n\n\nPlease enter a Username:\n')

                # checking whether the given username is unique or not.
                with open('scores.txt', 'r') as file:
                    IDs = []
                    lis = file.read().split(':')

                    for i in range(0, len(lis), 2):
                            IDs.append(lis[i])

                if username in IDs:
                    print('The username you entered already exists. Press enter to go back. ')


                else:
                    clearscreen()
                    print(f'\n\nWelcome to the game HANGMAN: {username}')
                    with open('words.txt', 'r') as f:      # opens the file containing words.
                       f = f.read()
                       word_list = f.split()

                    secret_word = random.choice(word_list)      # a random word is selected from the list of words made from file.
                    L = ['_ '] * len(secret_word)
                    available_letter = "abcdefghijklmnopqrstuvwxyz"
                    available_letter = [str(i) for i in available_letter]       # a list of available letters
                    D = {}
                    guess = 6
                    warning = 3
                    print(f'\nI am thinking of the word that is {len(secret_word)} letters long')
                    print(f'You have {warning} warnings left.')
                    print('-' * 70)
                    already_guess = []
                    unique_word = ''
                    while True:  # game
                        print("-" * 70)
                        guessed = ''.join(L)
                        print(f'You have {guess} guesses left')
                        print('Available Letter:', ''.join(available_letter))

                        # The guess is taken from the player.
                        letter = input('Enter your guess: ').lower().strip()
                        if letter in available_letter and letter not in already_guess:
                            already_guess.append(letter)        # The used letter is appended in a list
                            available_letter.remove(letter)      # and removed from the list of available letters

                            # if the guess is correct.
                            if letter in secret_word:
                                unique_word += letter

                                #the '_' is replaced with the guessed letter incase of correct guess.
                                for i in range(len(secret_word)):
                                    if secret_word[i] == letter:
                                        L[i] = letter
                                print(f"Good guess: {''.join(L)}\n")

                            else:


                                if letter in 'aeiou':       # if the incorrect letter is a vowel then 2 guesses are deducted.
                                    guess -= 2


                                else:               # if it is not a vowel, 1 guess is deducted.
                                    guess -= 1
                                print(f"Oops! This letter is not in my word: {guessed}")
                                hangman(guess)
                                print()


                        elif letter in already_guess or not (letter.isalpha()):     # conditions for invalid characters or letters that are already guessed

                            if warning != 0:
                                warning -= 1
                                print(f'You have {warning} warnings left')
                            else:
                                guess -= 1
                                hangman(guess)
                            if letter in already_guess:
                                print(f'You have already guessed this letter: {guessed}')
                                print()
                            else:
                                print(f'Invalid letter: {guessed}')
                                print()

                        # conditions if the player has won the game.
                        if '_ ' not in L:
                            print("CONGRATULATION!!!! YOU HAVE WON")
                            Total_Score = len(unique_word) * guess
                            print(f"Score: {Total_Score}")
                            with open('scores.txt', 'a') as f:
                                f.write(f'{username}:{Total_Score}\n')  # Username and Score are appended in scores.txt file.

                            # The Total score is compared to the other scores to check if the player has scored a HIGH SCORE.
                            with open('scores.txt') as f:
                                for i in f:
                                    name, score = i.split(":")
                                    D[name] = int(score)
                                highest_score = max(D.values())
                                if Total_Score > highest_score:
                                    print("\nHIGH SCORE !!")
                            input("\n\nPress Enter to return to go back !")
                            clearscreen()
                            break

                        # If the player loses the game then the game finishes
                        elif guess <= 0:  # or guess == -1:
                            print(f'Secret Word: {secret_word}\n\nYOU RAN OUT OF GUESSES !')
                            input('\n\npress Enter to go back.')
                            clearscreen()
                            break

                break

            # if the player wants to display scores.
            elif player_options == '2':
                scores = {}
                new_scores = {}

                # the file containing scores is opened and it is then sorted to display.
                with open("scores.txt") as f:
                    for line in f:
                        ls = line.split(':')
                        scores[ls[0]] = int(ls[1])
                sorted_values = sorted(scores.values(), reverse=True)
                for i in sorted_values:
                    for key, value in scores.items():
                        if value == i:
                            new_scores[key] = value

                # displays the socres with usernames.
                for i in new_scores:
                    print(i, '---------------', scores.get(i))

                input('\n\nPress any key to go back.\n')
                clearscreen()
                break


            # if player wants to know the rules
            elif player_options == '3':

                # The file containing rules is opened and printed on the screen.
                with open("Rules.txt") as f:
                    print(f.read())
                input('\n\nPress Enter to go back.\n')
                clearscreen()
                break

            #if the player wants to go back to previous menu.
            elif player_options == 'b':
                clearscreen()
                break

            # condition for any invalid inputs.
            else:
                print('Invalid key pressed !!')
                clearscreen()
                break
        break


