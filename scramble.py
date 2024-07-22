
# Imported the list of words stored from baseclass page.
from baseclass import *


def scramble_game():
    player1 = input("Enter a word: ").lower()

    # created empty lists to have a track of repeating word and for the major case statement.
    player1_entered_words = []
    player2_entered_words = []

    while player1 != "endgame":

        # Case statement for the first move of the game
        if len(player1_entered_words) == 0 and len(player2_entered_words) == 0:
            player1_entered_words.append(player1)

            if player1 not in words:
                words.append(player1)
            else:
                continue
        else:
            player1 = input("Enter a word which starts with the last character of the last word in the player2 "
                            "entered word,if it is the start of the game enter any word : ").lower()

            # Checks if player wants to end the game.
            if player1 != "endgame":

                # Checks if player has repeated the word, which results in end of the game.
                if player1 in player1_entered_words:
                    print("Game over, you repeated a word which you used before.")
                    break

                else:

                    # Checks if the entered word is starting from the character of the opposite player last character
                    # of last word.
                    if player1[0] == player2_entered_words[-1][-1]:
                        player1_entered_words.append(player1)

                        if player1[0] == player2_entered_words[-1][-1] and player1 not in words:
                            words.append(player1)

                    else:
                        print(f"Please enter a word which startswith '{player2_entered_words[-1][-1]}'")
                        player1 = input("Enter a word: ").lower()
                        if player1[0] == player2_entered_words[-1][-1]:
                            player1_entered_words.append(player1)

                            if player1[0] == player2_entered_words[-1][-1] and player1 not in words:
                                words.append(player1)

            else:
                print("You have entered the 'endgame' word to end the game, Game is now over.")
                break

        player2 = input("Enter a word which starts with the last character of the last word in the player1 entered "
                        "word: ").lower()

        if len(player1_entered_words) != 0 and len(player2_entered_words) == 0:

            if player2 != "endgame":

                if player2 in player2_entered_words:
                    print("Game over, you repeated a word which you used before.")
                    break
                else:

                    # Checks if the entered word is starting from the character of the opposite player last character
                    # of last word.

                    if player2[0] == player1_entered_words[-1][-1]:
                        player2_entered_words.append(player2)

                        if player2[0] == player1_entered_words[-1][-1] and player2 not in words:
                            words.append(player2)

                    else:
                        print(f"Please enter a word which startswith '{player1_entered_words[-1][-1]}'")
                        player2 = input("Enter a word: ").lower()
                        if player2[0] == player1_entered_words[-1][-1]:
                            player2_entered_words.append(player2)

                            if player2[0] == player1_entered_words[-1][-1] and player2 not in words:
                                words.append(player2)

            else:
                print("You have entered the 'endgame' word to end the game, Game is now over.")
                break

        else:
            if player2 != "endgame":

                if player2 in player2_entered_words:
                    print("Game over, you repeated a word which you used before.")
                    break
                else:

                    # Checks if the entered word is starting from the character of the opposite player last character
                    # of last word.

                    if player2[0] == player1_entered_words[-1][-1]:
                        player2_entered_words.append(player2)

                        if player2[0] == player1_entered_words[-1][-1] and player2 not in words:
                            words.append(player2)

                    else:
                        print(f"Please enter a word which startswith '{player1_entered_words[-1][-1]}'")
                        player2 = input("Enter a word: ").lower()
                        if player2[0] == player1_entered_words[-1][-1]:
                            player2_entered_words.append(player2)

                            if player2[0] == player1_entered_words[-1][-1] and player2 not in words:
                                words.append(player2)

            else:
                print("You have entered the 'endgame' word to end the game, Game is now over.")
                break

        print(player1_entered_words)
        print(player2_entered_words)
        print(words)

    answer = input("Do you want to play the game again?(y/n)").lower()

# To check if the players want to start the game again.
    while answer:
        if answer == "y":
            scramble_game()
        elif answer == "n":
            print("Thank you so much for playing the game")
            break
        else:
            print("Please enter 'y' or 'n'")
            answer = input("Do you want to play the game again?(y/n)").lower()


scramble_game()
