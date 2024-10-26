# Football Results

# Input the results of three football matches in the format "teamGoals:opponentGoals"
firstMatchResult = input("Enter the first match result (format: teamGoals:opponentGoals): ")
secondMatchResult = input("Enter the second match result (format: teamGoals:opponentGoals): ")
thirdMatchResult = input("Enter the third match result (format: teamGoals:opponentGoals): ")

# Initialize counters for wins, defeats, and draws
wins = 0
defeats = 0
draws = 0

# Function to process each match result and update win/lose/draw counts
def process_match(result):
    global wins, defeats, draws
    teamGoals, opponentGoals = map(int, result.split(":"))  # Split and convert to integers
    if teamGoals > opponentGoals:
        wins += 1  # Increment wins if team scored more
    elif teamGoals < opponentGoals:
        defeats += 1  # Increment defeats if opponent scored more
    else:
        draws += 1  # Increment draws if scores are equal

# Process each match result
process_match(firstMatchResult)
process_match(secondMatchResult)
process_match(thirdMatchResult)

# Output the final counts of wins, defeats, and draws
print(f"Team won {wins} games.")
print(f"Team lost {defeats} games.")
print(f"Drawn games: {draws}")
