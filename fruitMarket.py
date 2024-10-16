#1. Fruit Market
strawberriesPrice = float(input());
bananasAmount = float(input());
orangesAmount = float(input());
raspberriesAmount = float(input());
strawberriesAmount = float(input());

bill = strawberriesAmount * strawberriesPrice + raspberriesAmount * (strawberriesPrice / 2) + orangesAmount * (strawberriesPrice / 2 * 0.6) + bananasAmount * (strawberriesPrice / 2 * 0.2)
print(f"{bill:.2f}")