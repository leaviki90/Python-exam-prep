# Family Trip Budget Calculator

# Input: The current budget, number of nights, price per night, and additional cost percentage
currentBudget = float(input("Enter the family's budget in USD: "))
nightsNum = int(input("Enter the number of nights: "))
pricePerNight = float(input("Enter the price per night in USD: "))
additionalCostPercent = int(input("Enter the additional costs percentage: "))

# Initialize variables for tracking costs
moneyLeft = 0
nightsCost = 0

# Calculate the additional cost based on the percentage of the current budget
additionalCost = (currentBudget * additionalCostPercent) / 100

# Apply a discount if staying for more than 7 nights
if nightsNum > 7:
    pricePerNight *= 0.95

# Calculate total cost of nights and remaining money after expenses
nightsCost = nightsNum * pricePerNight
moneyLeft = currentBudget - nightsCost - additionalCost

# Determine if the budget is sufficient or if additional funds are needed
if moneyLeft >= 0:
    print(f"Smiths will be left with {moneyLeft:.2f} USD after vacation.")
else:
    print(f"{abs(moneyLeft):.2f} USD needed.")
