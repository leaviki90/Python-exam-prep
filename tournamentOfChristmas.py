# Tournament of Christmas

# Input the number of tournament days
tournamentDays = int(input("Enter the number of tournament days: "))

# Initialize variables to track the total money won, total wins, and total losses
totalMoneyWon = 0
totalWinCount = 0
totalLoseCount = 0

# Loop over each day of the tournament
for day in range(tournamentDays):
    # Initialize daily variables for wins, losses, and money earned per day
    winCount = 0
    loseCount = 0
    moneyPerDay = 0

    # Loop to process each sport played in a single day
    while True:
        sport = input("Enter sport name (or 'Finish' to end the day): ")

        # Break the loop if "Finish" is entered, signaling the end of the day
        if sport == "Finish":
            break

        # Input the result for the sport
        result = input("Enter result (win/lose): ")

        # Update counts and money based on result
        if result == "win":
            winCount += 1  # Increment daily win count
            moneyPerDay += 20  # Add $20 for each win
        elif result == "lose":
            loseCount += 1  # Increment daily loss count

    # Apply a 10% bonus to daily earnings if there are more wins than losses for the day
    if winCount > loseCount:
        moneyPerDay *= 1.10  # Increase daily money by 10%

    # Add daily results to the tournament totals
    totalMoneyWon += moneyPerDay
    totalWinCount += winCount
    totalLoseCount += loseCount

# Apply a 20% bonus to the total money if there were more wins than losses overall
if totalWinCount > totalLoseCount:
    totalMoneyWon *= 1.20
    print(f"You won the tournament! Total raised money: {totalMoneyWon:.2f}")
else:
    print(f"You lost the tournament. Total raised money: {totalMoneyWon:.2f}")
