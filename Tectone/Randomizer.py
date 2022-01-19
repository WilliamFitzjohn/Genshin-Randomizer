from pickletools import pyfrozenset
import random
enemyListOne = []
enemyListTwo = []
itemListOne = []
itemListTwo = []
pickedNums = []
pickedNumsI = []
enemyNum = 0
print("Welcome to the scuffed remake of Tectone's Randomizer!") #Intro to the program
print("Now including Inazuma and Enkanomiya!")
print("")
print("")

enemyInput = input("Please type '1' for all enemies to be in selection pool, or '2' for only harder enemies.")
check = int(enemyInput)
while check > 2 or check < 1:
    enemyInput = input("Can player 1 either type '1' or '2' (1 for heads, 2 for tails): ") #Player input for coin flip
    check = int(enemyInput)
print("")
print("")

if(check == 1):
    f = open("AllEnemyList.txt", "r") #opening the enemy list
    enemies = f.read().splitlines()
    f.close()
    enemyNum = 52
else:
    f = open("HardEnemyList.txt", "r") #opening the enemy list
    enemies = f.read().splitlines()
    f.close()
    enemyNum = 38

if(check == 1):
    f = open("AllEnemyList.txt", "r") #opening the enemy list
    enemies = f.read().splitlines()
    f.close()
    enemyNum = 52
else:
    f = open("HardEnemyList.txt", "r") #opening the enemy list
    enemies = f.read().splitlines()
    f.close()
    enemyNum = 38

f = open("Items.txt", "r") #opening the item list
items = f.read().splitlines()
f.close()

print("")
print("")
coin = input("Can player 1 either type '1' or '2' (1 for heads, 2 for tails): ")
check = int(coin)
while check > 2 or check < 1:
    coin = input("Can player 1 either type '1' or '2' (1 for heads, 2 for tails): ") #Player input for coin flip
    check = int(coin)
print("")
print("")

coinflip = random.randint(1,2)
if(coinflip == check):
    flower = input("Player 1 wins the coin flip! Type '1' to choose Pyro flower or '2' for Cyro flower: ")
    checkF = int(flower)
    while checkF > 2 or checkF < 1:
        flower = input("Player 1 wins the coin flip! Type '1' to choose Pyro flower or '2' for Cyro flower: ")
        checkF = int(flower)
    if(checkF == 1):
        flowerOne = "Pyro Flower"
        flowerTwo = "Cyro Flower"
    else:
        flowerTwo = "Pyro Flower"
        flowerOne = "Cyro Flower"
else:
    flower = input("Player 2 wins the coin flip! Type '1' to choose Pyro flower or '2' for Cyro flower: ")
    checkF = int(flower)
    while checkF > 2 or checkF < 1:
        flower = input("Player 2 wins the coin flip! Type '1' to choose Pyro flower or '2' for Cyro flower: ")
        checkF = int(flower)
    if(checkF == 1):
        flowerTwo = "Pyro Flower"
        flowerOne = "Cyro Flower"
    else:
        flowerOne = "Pyro Flower"
        flowerTwo = "Cyro Flower"
print("")
print("")

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

for i in range(0,5): #selecting items for player one
    n = random.randint(0,71)
    if(n not in pickedNumsI):
        itemListOne.append(items[n])
        pickedNumsI.append(n)
    else:
        while(n in pickedNumsI): #make sure there are no repeats in each player's pools
            n = random.randint(0,71)
        itemListOne.append(items[n])
        pickedNumsI.append(n)

for i in range(0,5): #selecting items for player one
    n = random.randint(0,71)
    if(n not in pickedNumsI):
        itemListTwo.append(items[n])
        pickedNumsI.append(n)
    else:
        while(n in pickedNumsI): #make sure there are no repeats in each player's pools
            n = random.randint(0,71)
        itemListTwo.append(items[n])
        pickedNumsI.append(n)

print("Player 1 Starts at:", flowerOne)
print("Player 1 Enemies:", enemyListOne)
print("Player 1 Items:", itemListOne)
print(" ")
print("Player 2 Starts at:", flowerTwo)
print("Player 2 Enemies:", enemyListTwo)
print("Player 2 Items:", itemListTwo)