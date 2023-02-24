s = int(input())
p = int(input())

for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(x, y)

