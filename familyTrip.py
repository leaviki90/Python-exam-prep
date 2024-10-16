#2. Family Trip

currentBudget = float(input())
nightsNum = int(input())
pricePerNight = float(input())
additionalCostPercent = int(input())
moneyLeft = 0
nightsCost = 0


additionalCost = (currentBudget * additionalCostPercent) / 100

if nightsNum > 7:
    pricePerNight = pricePerNight * 0.95

nightsCost = nightsNum * pricePerNight
moneyLeft = currentBudget - nightsCost - additionalCost
if moneyLeft >= 0:
       print(f"Smiths will be left with {moneyLeft:.2f} USD after vacation.")
else:
       print(f"{abs(moneyLeft):.2f} USD needed.")