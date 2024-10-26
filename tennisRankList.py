# Tennis RankList

# Points distribution:
# W - Winner: receives 2000 points
# F - Finalist: receives 1200 points
# SF - Semi-finalist: receives 720 points

# Input: number of tournaments played
tournamentsNum = int(input("Enter the number of tournaments: "))

# Input: starting points in the ranking
initialPoints = int(input("Enter initial ranking points: "))

# Initialize counters for wins and total points gained during tournaments
winnerCount = 0
tournamentPoints = 0

# Loop through each tournament to gather results
for tournament in range(tournamentsNum):
    # Input the stage reached in the current tournament
    tournamentStage = input("Enter the tournament result (W, F, or SF): ")

    # Check result and update points accordingly
    if tournamentStage == "W":
        winnerCount += 1  # Count this as a win
        tournamentPoints += 2000  # Add points for a win
    elif tournamentStage == "F":
        tournamentPoints += 1200  # Add points for reaching the final
    elif tournamentStage == "SF":
        tournamentPoints += 720  # Add points for reaching the semi-final

# Calculate the final points after all tournaments
finalPoints = initialPoints + tournamentPoints
print(f"Final points: {finalPoints}")

# Calculate the average points per tournament (integer division for whole points)
averagePoints = tournamentPoints // tournamentsNum
print(f"Average points: {averagePoints}")

# Calculate the win percentage across all tournaments
winPercentage = (winnerCount / tournamentsNum) * 100
print(f"{winPercentage:.2f}%")
