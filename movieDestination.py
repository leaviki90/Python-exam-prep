#3. Movie Destination

movieBudget = float(input())
destination = input().capitalize()
season = input().capitalize()

shootingDays = int(input())
price = 0

#        Dubai	   Washington	London
#Winter	45 000 USD.	17 000 USD.	24 000 USD.
#Summer	40 000 USD.	12 500 USD.	20 250 USD.

if destination == "Dubai":
    if season == "Winter":
      price = shootingDays * 45000
    elif season == "Summer":
        price = shootingDays * 40000
elif destination == "Washington":
    if season == "Winter":
        price = shootingDays * 17000
    elif season == "Summer":
        price = shootingDays * 12500
elif destination == "London":
    if season == "Winter":
        price = shootingDays * 24000
    elif season == "Summer":
        price = shootingDays * 20250
if season not in ("Winter", "Summer"):
    print("Invalid season!")
    exit()

if destination not in ("Dubai", "Washington", "London"):
    print("Invalid destination!")
    exit()
if destination == "Dubai":
    price = price * 0.7
elif destination == "Washington":
    price = price * 1.25

if price <= movieBudget:
      print(f"The budget for the movie is enough! We have {(movieBudget - price):.2f} USD left!")
else:
      print(f"The director needs {abs(movieBudget - price):.2f} USD more!")
