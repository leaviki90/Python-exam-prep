# Easter Eggs Battle

# Input the initial number of eggs each player has
firstPlayerEggs = int(input("Enter the number of eggs for Player One: "))
secondPlayerEggs = int(input("Enter the number of eggs for Player Two: "))

# Start a loop for the egg battle
while True:
    # Input the winner of each round, or "End" to finish the game
    winnerText = input("Enter the round winner ('one' or 'two'), or 'End' to finish the game: ")

    # If the game ends, print the remaining eggs for both players
    if winnerText == "End":
        print(f"Player one has {firstPlayerEggs} eggs left.")
        print(f"Player two has {secondPlayerEggs} eggs left.")
        break

    # Check if the winner input is valid
    if winnerText not in ("one", "two"):
        print("Invalid winner type! Please enter 'one', 'two', or 'End'.")
        exit()

    # Deduct an egg from the losing player based on the winner of the round
    if winnerText == "one":
        secondPlayerEggs -= 1
        # Check if Player Two has run out of eggs
        if secondPlayerEggs == 0:
            print(f"Player two is out of eggs. Player one has {firstPlayerEggs} eggs left.")
            break
    else:
        firstPlayerEggs -= 1
        # Check if Player One has run out of eggs
        if firstPlayerEggs == 0:
            print(f"Player one is out of eggs. Player two has {secondPlayerEggs} eggs left.")
            break
