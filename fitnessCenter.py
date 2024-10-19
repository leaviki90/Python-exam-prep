# Fitness Center - tracks visitor activities (workouts and protein purchases) and calculates percentages

visitors = int(input())  # Number of visitors is input as an integer
# Initialize counters for different workout activities and protein purchases
countBack = 0
countChest = 0
countLegs = 0
countAbs = 0
countPShake = 0
countPBar = 0

# Loop through each visitor to record their activity
for visitors in range(1, visitors + 1):
    activity = input()  # Input activity for each visitor
    # Increase the respective counter based on the activity
    if activity == "Back":
        countBack += 1
    if activity == "Chest":
        countChest += 1
    if activity == "Legs":
        countLegs += 1
    if activity == "Abs":
        countAbs += 1
    if activity == "Protein shake":
        countPShake += 1
    if activity == "Protein bar":
        countPBar += 1

# Calculate total workout and protein purchases
workout = countBack + countChest + countLegs + countAbs  # Sum up all workout activities
proteinPurchase = countPShake + countPBar  # Sum up protein shake and bar purchases

# Print the count for each activity
print(f"{countBack} - back")
print(f"{countChest} - chest")
print(f"{countLegs} - legs")
print(f"{countAbs} - abs")
print(f"{countPShake} - protein shake")
print(f"{countPBar} - protein bar")

# Calculate and print the percentage of visitors who worked out and who bought protein
print(f"{(workout / visitors) * 100:.2f}% - work out")
print(f"{(proteinPurchase / visitors) * 100:.2f}% - protein")
