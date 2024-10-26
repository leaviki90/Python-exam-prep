# Input the budget for the movie
movieBudget = float(input())  # Movie budget in USD

# Input the destination and season, capitalize them for consistency
destination = input().capitalize()  # Destination where the movie will be shot
season = input().capitalize()  # Season during which the shooting takes place

# Input the number of shooting days
shootingDays = int(input())  # Total number of days for the movie shooting

# Initialize the price to 0
price = 0

# Define the shooting costs based on the destination and season:
# - Dubai: 45,000 USD per day in Winter, 40,000 USD per day in Summer
# - Washington: 17,000 USD per day in Winter, 12,500 USD per day in Summer
# - London: 24,000 USD per day in Winter, 20,250 USD per day in Summer

if destination == "Dubai":
    if season == "Winter":
        price = shootingDays * 45000  # Calculate price for Dubai in Winter
    elif season == "Summer":
        price = shootingDays * 40000  # Calculate price for Dubai in Summer
elif destination == "Washington":
    if season == "Winter":
        price = shootingDays * 17000  # Calculate price for Washington in Winter
    elif season == "Summer":
        price = shootingDays * 12500  # Calculate price for Washington in Summer
elif destination == "London":
    if season == "Winter":
        price = shootingDays * 24000  # Calculate price for London in Winter
    elif season == "Summer":
        price = shootingDays * 20250  # Calculate price for London in Summer

# Validate season input; exit if the season is invalid
if season not in ("Winter", "Summer"):
    print("Invalid season!")
    exit()

# Validate destination input; exit if the destination is invalid
if destination not in ("Dubai", "Washington", "London"):
    print("Invalid destination!")
    exit()

# Apply discounts and markups:
# - Dubai gets a 30% discount
# - Washington gets a 25% markup
if destination == "Dubai":
    price = price * 0.7  # 30% discount for Dubai
elif destination == "Washington":
    price = price * 1.25  # 25% markup for Washington

# Compare the calculated price with the movie budget
if price <= movieBudget:
    # If the budget is enough, print the remaining amount
    print(f"The budget for the movie is enough! We have {(movieBudget - price):.2f} USD left!")
else:
    # If the budget is not enough, print how much more is needed
    print(f"The director needs {abs(movieBudget - price):.2f} USD more!")
