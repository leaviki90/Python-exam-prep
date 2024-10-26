# Excursion Calculator

# Input the number of people in the group and the season
peopleNumber = int(input("Enter the number of people: "))
season = input("Enter the season (spring, summer, autumn, winter): ").lower()

# Initialize base price and total price variables
price = 0
totalPrice = 0

# Determine base price per person based on season and group size
if season == "spring":
    price = peopleNumber * (50 if peopleNumber <= 5 else 48)
elif season == "summer":
    price = peopleNumber * (48.5 if peopleNumber <= 5 else 45)
elif season == "autumn":
    price = peopleNumber * (60 if peopleNumber <= 5 else 49.5)
elif season == "winter":
    price = peopleNumber * (86 if peopleNumber <= 5 else 85)
else:
    print("error: invalid season")
    exit()

# Apply discounts or increases based on season
totalPrice = price
if season == "summer":
    totalPrice *= 0.85  # Apply 15% discount for summer
elif season == "winter":
    totalPrice *= 1.08  # Apply 8% increase for winter

# Round to 2 decimal places and display the final price
print(f"{totalPrice:.2f} USD.")
