# Prompt the user to enter the number of days and the total amount of food available for the pets
numbOfDays = int(input())  # Number of days to track the food consumption
foodAmount = float(input())  # Total amount of food in grams

# Initialize variables to track the total food consumed, biscuits, and individual pet consumption
eatenBiscuitsAmount = 0  # Keeps track of the biscuits given every 3rd day
countDays = 0  # Counts the days as the loop progresses
eatenFood = 0  # Total amount of food eaten by both pets
eatenFoodByDog = 0  # Total amount of food eaten by the dog
eatenFoodByCat = 0  # Total amount of food eaten by the cat

# Loop through each day to get food consumption by the dog and the cat
for i in range(1, numbOfDays + 1):
    dogFood = int(input())  # Food eaten by the dog on this day
    catFood = int(input())  # Food eaten by the cat on this day

    # Add today's food consumption to the total food consumption for both pets
    eatenFood += dogFood + catFood
    eatenFoodByDog += dogFood  # Add today's dog food to the total
    eatenFoodByCat += catFood  # Add today's cat food to the total

    countDays += 1  # Increment the day count

    # Every 3rd day, add 10% of the food eaten on that day as biscuits
    if countDays % 3 == 0:
        eatenBiscuitsAmount += (dogFood + catFood) * 0.1  # Calculate biscuits amount for this day

# Calculate percentages for total food eaten, dog food eaten, and cat food eaten
totalEatenFood = eatenFood / foodAmount * 100  # Percentage of total food eaten compared to food available
eatenFoodByDog = eatenFoodByDog / eatenFood * 100  # Percentage of total food eaten by the dog
eatenFoodByCat = eatenFoodByCat / eatenFood * 100  # Percentage of total food eaten by the cat

# Print the results in the desired format
print(f"Total eaten biscuits: {round(eatenBiscuitsAmount)}gr.")  # Total biscuits given, rounded to the nearest gram
print(f"{totalEatenFood:.2f}% of the food has been eaten.")  # Total percentage of food eaten
print(f"{eatenFoodByDog:.2f}% eaten from the dog.")  # Percentage of food eaten by the dog
print(f"{eatenFoodByCat:.2f}% eaten from the cat.")  # Percentage of food eaten by the cat
