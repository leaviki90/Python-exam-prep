# Cat Diet Calculator

# Constants for calorie content per gram of each macronutrient
# 1 gram of fat = 9 calories
# 1 gram of protein = 4 calories
# 1 gram of carbohydrate = 4 calories

# Input percentages and total calories for the diet
fatPercentage = int(input("Enter the fat percentage: "))
proteinPercentage = int(input("Enter the protein percentage: "))
carboPercentage = int(input("Enter the carbohydrate percentage: "))
totalCalories = int(input("Enter the total calories in the diet: "))
waterPercentage = int(input("Enter the water percentage in the diet: "))

# Calculate the grams of each macronutrient in the diet
# Fat grams calculation based on calorie contribution and calorie content per gram
fat = totalCalories * (fatPercentage / 100) / 9

# Protein grams calculation based on calorie contribution and calorie content per gram
protein = totalCalories * (proteinPercentage / 100) / 4

# Carbohydrate grams calculation based on calorie contribution and calorie content per gram
carbohydrates = totalCalories * (carboPercentage / 100) / 4

# Calculate total food weight excluding water
foodWeight = fat + protein + carbohydrates

# Calculate calories per gram of food excluding water
caloriesPerGram = totalCalories / foodWeight

# Adjust for water content in the diet
caloriesPerGram *= (1 - waterPercentage / 100)

# Output the result rounded to four decimal places
print(f"{caloriesPerGram:.4f}")
