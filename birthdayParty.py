# Birthday party - calculate the total cost for a birthday party based on hall rent and other related expenses

hallRent = float(input())  # The user is prompted to input the hall rent (a floating point number)

# Cake – its price is 20% of the hall rent
cake = hallRent * 0.20  # The cake price is calculated as 20% of the hall rent

# Drinks – their price is 45% less than the one of the cake
drinks = cake * 0.55  # The drink price is calculated as 55% of the cake price (45% less)

# Entertainer – its price is 1/3 of hall rent
entertainer = hallRent / 3  # The entertainer's fee is calculated as one-third of the hall rent

# Total budget needed for the birthday party
neededBudget = hallRent + cake + drinks + entertainer  # Sum up all expenses: hall rent, cake, drinks, and entertainer

# Print the total budget with one decimal precision
print(f"{neededBudget:.1f}")  # Print the total budget formatted to one decimal place
