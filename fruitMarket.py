# Get the price per kilogram of strawberries
strawberriesPrice = float(input())  # Price of strawberries per kg

# Get the amount (in kg) of each fruit the customer is buying
bananasAmount = float(input())  # Amount of bananas in kg
orangesAmount = float(input())  # Amount of oranges in kg
raspberriesAmount = float(input())  # Amount of raspberries in kg
strawberriesAmount = float(input())  # Amount of strawberries in kg

# Calculate the total bill:
# - The cost of strawberries is straightforward (strawberriesAmount * strawberriesPrice).
# - Raspberries cost half the price of strawberries (strawberriesPrice / 2).
# - Oranges cost 60% of the raspberry price ((strawberriesPrice / 2) * 0.6).
# - Bananas cost 20% of the raspberry price ((strawberriesPrice / 2) * 0.2).
bill = (
    strawberriesAmount * strawberriesPrice +  # Total cost of strawberries
    raspberriesAmount * (strawberriesPrice / 2) +  # Total cost of raspberries
    orangesAmount * (strawberriesPrice / 2 * 0.6) +  # Total cost of oranges
    bananasAmount * (strawberriesPrice / 2 * 0.2)  # Total cost of bananas
)

# Output the total bill, formatted to 2 decimal places
print(f"{bill:.2f}")
