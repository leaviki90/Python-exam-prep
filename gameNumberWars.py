# Number Wars - a game where two players compare cards and gain points

firstPlayerName = input()  # Input first player's name
secondPlayerName = input()  # Input second player's name
firstPlayerPoints = 0  # Initialize the first player's points
secondPlayerPoints = 0  # Initialize the second player's points

# Start the game loop
while True:
    fPcard = input()  # Input card from the first player
    if fPcard == "End of game":  # Check if the game should end
        # Print both players' points and exit the loop
        print(f"{firstPlayerName} has {firstPlayerPoints} points")
        print(f"{secondPlayerName} has {secondPlayerPoints} points")
        break

    sPcard = input()  # Input card from the second player
    if sPcard == "End of game":  # Check if the game should end
        # Print both players' points and exit the loop
        print(f"{firstPlayerName} has {firstPlayerPoints} points")
        print(f"{secondPlayerName} has {secondPlayerPoints} points")
        break

    # Convert the card inputs to integers
    fPcard = int(fPcard)
    sPcard = int(sPcard)

    # Compare the cards
    if fPcard > sPcard:
        # The first player wins the round, points are calculated based on the difference
        firstPlayerPoints += fPcard - sPcard
    elif sPcard > fPcard:
        # The second player wins the round, points are calculated based on the difference
        secondPlayerPoints += sPcard - fPcard
    else:
        # If both cards are equal, trigger "Number wars"
        print("Number wars!")
        fPcard = int(input())  # New card for the first player
        sPcard = int(input())  # New card for the second player

        # Determine the winner of the "Number wars"
        if fPcard > sPcard:
            print(f"{firstPlayerName} is winner with {firstPlayerPoints} points")
        else:
            print(f"{secondPlayerName} is winner with {secondPlayerPoints} points")
        break  # End the game after "Number wars"
