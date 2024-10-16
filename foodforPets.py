#4. Food for Pets

numbOfDays = int(input())
foodAmount = float(input())
eatenBiscuitsAmount = 0;
countDays = 0
eatenFood = 0
eatenFoodByDog = 0
eatenFoodByCat = 0


for i in range(1, numbOfDays + 1):
    dogFood = int(input())
    catFood = int(input())
    eatenFood += dogFood + catFood
    eatenFoodByDog += dogFood
    eatenFoodByCat += catFood
    countDays += 1
    if countDays % 3 == 0:
        eatenBiscuitsAmount += (dogFood + catFood) * 0.1

totalEatenFood = eatenFood / foodAmount * 100
eatenFoodByDog = eatenFoodByDog / eatenFood * 100
eatenFoodByCat = eatenFoodByCat / eatenFood * 100

print(f"Total eaten biscuits: {round(eatenBiscuitsAmount)}gr.")
print(f"{totalEatenFood:.2f}% of the food has been eaten.")
print(f"{eatenFoodByDog:.2f}% eaten from the dog.")
print(f"{eatenFoodByCat:.2f}% eaten from the cat.")
