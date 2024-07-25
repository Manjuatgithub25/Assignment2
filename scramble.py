
# Imported the list of words stored from baseclass page.
from baseclass import *


def scramble_game():
    player1 = input("Enter a word: ")

    if player1.lower() == "endgame":
        print(f"You have entered '{player1}', so the game has ended")

    else:
        # created empty lists to have a track of repeating word and for the major case statement.
        players_entered_words = []

        while player1.lower() != "endgame":

            # Case statement for the first move of the game
            if len(players_entered_words) == 0:
                players_entered_words.append(player1)

                if player1 not in words:
                    words.append(player1)
            else:

                # Checks if player wants to end the game.
                if player1.lower() != "endgame":

                    # Checks if player has repeated the word, which results in end of the game.
                    if player1 in players_entered_words:
                        print(f"Game over, you repeated the word '{player1}' which you used before.")
                        break

                    else:
                        # Checks if the entered word is starting from the character of the opposite player last
                        # character of last word.
                        if player1[0] == players_entered_words[-1][-1]:
                            players_entered_words.append(player1)

                            if player1 not in words:
                                words.append(player1)

                        else:
                            print(f"Please enter a word which startswith '{players_entered_words[-1][-1]}'")
                            player1 = input("Enter a word: ").lower()
                            if player1[0] == players_entered_words[-1][-1]:
                                players_entered_words.append(player1)

                                if player1 not in words:
                                    words.append(player1)

                else:
                    print(f"You have entered the '{player1}' word to end the game, Game is now over.")
                    break

            player2 = input("Enter a word which starts with the last character of the last word in the players entered "
                            "word: ")

            if player2.lower() != "endgame":

                if player2 in players_entered_words:
                    print(f"Game over, you repeated the word '{player2}' which you used before.")
                    break
                else:

                    # Checks if the entered word is starting from the character of the opposite player last character
                    # of last word.

                    if player2[0] == players_entered_words[-1][-1]:
                        players_entered_words.append(player2)

                        if player2 not in words:
                            words.append(player2)

                    else:
                        print(f"Please enter a word which startswith '{players_entered_words[-1][-1]}'")
                        player2 = input("Enter a word: ").lower()
                        if player2[0] == players_entered_words[-1][-1]:
                            players_entered_words.append(player2)

                            if player2 not in words:
                                words.append(player2)

            else:
                print(f"You have entered the '{player2}' word to end the game, Game is now over.")
                break

            print(players_entered_words)
            print(words)

            player1 = input("Enter a word which starts with the last character of the last word in the player2 "
                            "entered word,if it is the start of the game enter any word : ")

            if player1 == "endgame":
                print(f"You have entered the '{player1}' word to end the game, Game is now over.")

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
