# Film premiere - calculates the total bill for purchasing movie tickets with specific discounts

movieName = input().title()  # Input movie name (converted to title case for consistency)
moviePackage = input().title()  # Input package option (Drink, Popcorn, Menu)
ticketsNumber = int(input())  # Input number of tickets
price = 0  # Initialize price variable

# Set price per ticket depending on the movie and the package chosen
if movieName == "John Wick":
    if moviePackage == "Drink":
        price = ticketsNumber * 12
    elif moviePackage == "Popcorn":
        price = ticketsNumber * 15
    elif moviePackage == "Menu":
        price = ticketsNumber * 19
elif movieName == "Star Wars":
    if moviePackage == "Drink":
        price = ticketsNumber * 18
    elif moviePackage == "Popcorn":
        price = ticketsNumber * 25
    elif moviePackage == "Menu":
        price = ticketsNumber * 30
elif movieName == "Jumanji":
    if moviePackage == "Drink":
        price = ticketsNumber * 9
    elif moviePackage == "Popcorn":
        price = ticketsNumber * 11
    elif moviePackage == "Menu":
        price = ticketsNumber * 14

# Validate the movie name; if invalid, terminate the program
if movieName not in ("John Wick", "Star Wars", "Jumanji"):
    print("Invalid movie name")
    exit()  # Exit if the movie name is invalid

# Validate the package name; if invalid, terminate the program
if moviePackage not in ("Drink", "Popcorn", "Menu"):
    print("Invalid movie package")
    exit()  # Exit if the package is invalid

# Set the final price initially as the base price (without discounts)
finalPrice = price

# Apply a 30% discount if the movie is Star Wars and at least 4 tickets are bought
if movieName == "Star Wars" and ticketsNumber >= 4:
    finalPrice = price * 0.70  # 30% family discount for Star Wars

# Apply a 15% discount if the movie is Jumanji and exactly 2 tickets are bought
if movieName == "Jumanji" and ticketsNumber == 2:
    finalPrice = price * 0.85  # 15% discount for Jumanji

# Output the final bill, formatted to 2 decimal places
print(f"Your bill is {finalPrice:.2f} USD.")


