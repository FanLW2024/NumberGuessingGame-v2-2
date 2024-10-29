## This file is designed to read and write to a file named "topPlayers.txt"

def updateTopPlayers(playerName, attempts, quit_game=False):
    if quit_game:
        return

    try:
        # Opening the "topPlayers.txt" file in read mode with r.
        with open("topPlayers.txt", "r") as file:
            # This will read the file line by line and split each line into a list of strings
            players = [line.strip().split() for line in file.readlines()]

        # Appending the new player and the attempts in the file
        players.append([str(attempts), playerName])

        # Sorting the players list based on the number of attempts in ascending order
        players.sort(key=lambda x: int(x[0]))

        # Keeping only 5 player In the list.
        top_players = players[:5]

        # Opening the "topPlayers.txt" file in writing mode.
        with open("topPlayers.txt", "w") as file:

            # This will write the updated list back to the file.
            for player in top_players:
                file.write(f"{player[0]} {player[1]}\n")

    except FileNotFoundError:

        # If the file is not found, it will create one and keep the record.
        with open("topPlayers.txt", "w") as file:
            file.write(f"{attempts} {playerName}\n")

# Displaying the list of top 5 players on the screen.
def displayTopPlayers():
    try:

        # Opening the updated "topPlayers.txt" file in read mode
        with open("topPlayers.txt", "r") as file:
            players = [line.strip().split() for line in file.readlines()]

        # Checking the player list, and if there is players than it will print the list.
        if not players:
            print(f"There is no top players. Play the game and you will be there!")
        else:
            print(f"Top Players:")
            for i, player in enumerate(players):
                score, name = player
                print(f"{i + 1}. {name} : {score} attempts.")

    except FileNotFoundError:
        print(f"There is no file to display!!")

    except EOFError:
        print("An error occurred while reading the top players file.")

