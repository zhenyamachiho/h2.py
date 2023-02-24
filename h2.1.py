import random
coins = [random.randint(0, 1) for i in range(0, int(input()))]
print(coins)
eagle = 0
tails = 0
for i in coins:
    if i == 0:
        eagle += 1
    else:
        tails += 1
if eagle > tails:
    print(tails)
else:
    print(eagle)


