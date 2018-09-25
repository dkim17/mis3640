import math


def mysqrt(a, x):
    while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y

for a in range (1,10):
    x = a *2

print(mysqrt(a, x))
print(math.sqrt(a))
math.sqrt(96)

diff = 'mysqrt(a)' - 'math.sqrt(a)'





