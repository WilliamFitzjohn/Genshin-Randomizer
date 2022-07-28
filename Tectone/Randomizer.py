import random
enemyListOne = []
enemyListTwo = []
itemListOne = []
itemListTwo = []
pickedNums = []
pickedNumsI = []
enemyNum = 0
print("Welcome to the scuffed remake of Tectone's Randomizer!") #Intro to the program
print("Now including Inazuma and Enkanomiya!\n")
print("RULES:")
print("#1 Both players present in same game (2 party members each)")
print("#2 Only fast travel is to statues of seven, MUST be at a statue to go to another.")
print("#3 Players END at Spiral Abyss (First one to touch the ground.")
print("#4 Items MUST be picked up.")
print("#5 No Food/Items.")
print("#6 No team swaps.")
print("#7 Mona is banned.")
print("#8 Players may ban 1 unit from others roster.\n")

#opening the enemy list
with open("HardEnemyList.txt", "r") as f:
    enemies = f.read().splitlines()
enemyNum = 39

#Open the item list
with open("Items.txt", "r") as f:
    items = f.read().splitlines()


print("Can player 1 either type '1' or '2' (1 for heads, 2 for tails): ")
coin = input(" ")
check = int(coin)
while check > 2 or check < 1:
    print("Can player 1 either type '1' or '2' (1 for heads, 2 for tails): ")
    coin = input(" ") #Player input for coin flip
    check = int(coin)
print("\n")

coinflip = random.randint(1,2)
if coinflip == check:
    print("Player 1 wins the coin flip! Type '1' to choose Pyro flower or '2' for Cyro flower:  ")
    flower = input(" ")
    checkF = int(flower)
    while checkF > 2 or checkF < 1:
        print("Player 1 wins the coin flip! Type '1' to choose Pyro flower or '2' for Cyro flower:  ")
        flower = input(" ")
        checkF = int(flower)
    if(checkF == 1):
        flowerOne = "Pyro Flower"
        flowerTwo = "Cyro Flower"
    else:
        flowerTwo = "Pyro Flower"
        flowerOne = "Cyro Flower"
else:
    print("Player 2 wins the coin flip! Type '1' to choose Pyro flower or '2' for Cyro flower: ")
    flower = input(" ")
    checkF = int(flower)
    while checkF > 2 or checkF < 1:
        print("Player 2 wins the coin flip! Type '1' to choose Pyro flower or '2' for Cyro flower: ")
        flower = input(" ")
        checkF = int(flower)
    if(checkF == 1):
        flowerTwo = "Pyro Flower"
        flowerOne = "Cyro Flower"
    else:
        flowerOne = "Pyro Flower"
        flowerTwo = "Cyro Flower"
print("\n")

for i in range(0,5): #selecting enemies for player one
    n = random.randint(0,enemyNum) 
    if(n not in pickedNums):
        enemyListOne.append(enemies[n])
        pickedNums.append(n)
    else:
        while(n in pickedNums): #make sure there are no repeats in each player's pools
            n = random.randint(0,53)
        enemyListOne.append(enemies[n])
        pickedNums.append(n)

for i in range(0,5): #selecting enemies for player one
    n = random.randint(0,enemyNum)
    if(n not in pickedNums):
        enemyListTwo.append(enemies[n])
        pickedNums.append(n)
    else:
        while(n in pickedNums): #make sure there are no repeats in each player's pools
            n = random.randint(0,enemyNum)
        enemyListTwo.append(enemies[n])
        pickedNums.append(n)

for _ in range(0,5): #selecting items for player one
    n = random.randint(0,60)
    if(n not in pickedNumsI):
        itemListOne.append(items[n])
        pickedNumsI.append(n)
    else:
        while(n in pickedNumsI): #make sure there are no repeats in each player's pools
            n = random.randint(0,60)
        itemListOne.append(items[n])
        pickedNumsI.append(n)

for _ in range(0,5): #selecting items for player one
    n = random.randint(0,60)
    if(n not in pickedNumsI):
        itemListTwo.append(items[n])
        pickedNumsI.append(n)
    else:
        while(n in pickedNumsI): #make sure there are no repeats in each player's pools
            n = random.randint(0,60)
        itemListTwo.append(items[n])
        pickedNumsI.append(n)

print("Player 1 Starts at:", flowerOne)
print("Player 1 Enemies:", enemyListOne)
print("Player 1 Items:", itemListOne, "\n")
print("Player 2 Starts at:", flowerTwo)
print("Player 2 Enemies:", enemyListTwo)
print("Player 2 Items:", itemListTwo)