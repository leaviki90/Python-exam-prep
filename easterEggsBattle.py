#5. Easter Eggs Battle

firstPlayerEggs = int(input())
secondPlayerEggs = int(input())

while True:
    winnerText = input()
    if winnerText == "End":
        print(f"Player one has {firstPlayerEggs} eggs left.")
        print(f"Player two has {secondPlayerEggs} eggs left.")
        break
    if winnerText not in ("one", "two"):
        print("Invalid winner type!")
        exit()
    if winnerText == "one":
        secondPlayerEggs -= 1
        if secondPlayerEggs == 0:
            print(f"Player two is out of eggs. Player one has {firstPlayerEggs} eggs left.")
            break
    else:
        firstPlayerEggs -= 1
        if firstPlayerEggs == 0:
            print(f"Player one is out of eggs. Player two has {secondPlayerEggs} eggs left.")
            break






