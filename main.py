# Lir-Wan Fan
# Purpose: Creating a number guessing game.
# Randomly choose a number between 1 and 100 (inclusive)
# Have the player enter a guess via input
# Tell the player the guess is high, low, or correct
# If high or low, allow the player to enter another guess
# Give the player an option to quit at any time
# Reward the player for a correct guess (ex., "Good job!")
# Tell the player how many guesses it took to guess correctly

# New Requirements: ######################################
# 1. Ask the player for their name prior to playing the game
# 2. After each game: Update a file called topPlayers.txt with the results of the game.
#     Only save the top five players and scores
#     Display the updated top 5 players from the topPlayers.txt file
#     Allow the player to play again without having to rerun the program
#     Use the topPlayers.txt.  Download topPlayers.txt file as a starting file
# 3. If you opt to use functions, move those functions into a single library file
# 4. Anticipate exceptions and catch them (i.e., fail nicely)
# 5. The game should feel like a nice game to play
#     Make it easy for the player to play the game
#     Do not make the player do a bunch of extra stuff to play
# 6. Specifications for topPlayers.txt
#     The file should only contain five (5) rows
#     Each row should contain two columns of information:
#         Column 1 should contain a score (i.e., number of guesses); Starts at position zero (0)
#         Column 2 should contain a player's name; Starts at position ten (10)
#     The file should be sorted, by column 1, lowest score (i.e., best score) to highest score

##################################################################################################

# Randomly choose a number between 1 and 100 (inclusive)
import random

from playerLibrary import updateTopPlayers, displayTopPlayers


random_number = random.randint(1, 100)
print(f"Randomly chose a number between 1 and 100 and this number will be unknown to the player: {random_number}")
print("-------------------------------------------------------------------------------------------")
print()

#Give the Player an option to add name.
playerName = input("Enter your name: ")
print(f"Welcome, {playerName}!")
print()
print("We have selected a number between 1 and 100.")

# Guess count for telling the player how many guesses it took to guess correctly
guess_count = 0

# Have the player enter a guess via input
while True:
    guess_number = input("Type in your guess number between 1 and 100 or 'q' to quit: ")

    try:
        guess_number = int(guess_number)
        guess_count += 1

        # Tell the player the guess is between 1 and 100
        if guess_number < 1 or guess_number > 100:
            print("The guess must be between 1 and 100.")
            print()
            continue

        # Tell the player the guess is too low
        if guess_number < random_number:
            print("Your guess is too low. Go up a little.")
            print()

        # Tell the player the guess is too high
        elif guess_number > random_number:
            print("Your guess is too high. Go down a little.")
            print()


        # Tell the player the guess is correct and reward the player for a correct guess
        # Tell the player how many guesses it took to guess correctly
        else:
            print(f"Good Job!! Congratulations!! You are the winner. It took you {guess_count} guesses.")
            updateTopPlayers(playerName, guess_count)
            displayTopPlayers()
            break

    except ValueError:

        if guess_number.lower() != 'q':
            print("Invalid input!")

        # Give the player an option to quit at any time
        if guess_number.lower() == 'q':
            print(f"Thank you very much. You took {guess_count} guesses. Better luck next time. Goodbye!")
            break

            # Checking the difference to give a clue for  the player.
            difference = (playerGuess - secretNumber)
            clue = abs(difference)
            if clue <= 5:
                print(f"Clue: You're getting closer!")
            # This is for exception.

        #except ValueError:
        print(f"Please enter a valid number.")



