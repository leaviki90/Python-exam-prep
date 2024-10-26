# Darts Game

# Initialize starting points and input player name
initialPoints = 301
playerName = input("Enter player name: ")

# Initialize total points, successful and unsuccessful throw counters
totalPoints = initialPoints
successfulThrows = 0
unSuccessfulThrows = 0

# Game loop continues until the player's points reach zero or they retire
while totalPoints > 0:
    # Input field type ("Single", "Double", "Triple", or "Retire")
    field = input("Enter field (Single, Double, Triple, or Retire): ")

    # Check if player decides to retire
    if field == "Retire":
        print(f"{playerName} retired after {unSuccessfulThrows} unsuccessful shots.")
        break

    # Input points scored for this throw
    points = int(input("Enter points: "))

    # Determine multiplier based on field type
    if field == "Single":
        multiplier = 1
    elif field == "Double":
        multiplier = 2
    elif field == "Triple":
        multiplier = 3
    else:
        print("Invalid input! Please enter 'Single', 'Double', 'Triple', or 'Retire'.")
        continue  # Skip to the next iteration if input is invalid

    # Calculate total points for this round
    totalPointsThisRound = points * multiplier

    # Update points if the throw doesn't exceed current total points
    if totalPointsThisRound <= totalPoints:
        totalPoints -= totalPointsThisRound
        successfulThrows += 1  # Increment successful throws
    else:
        unSuccessfulThrows += 1  # Increment unsuccessful throws if points exceeded

    # Check if player has won the leg
    if totalPoints == 0:
        print(f"{playerName} won the leg with {successfulThrows} shots.")
        break
