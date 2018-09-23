import math


def mysqrt(a, x):
    while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y

print(mysqrt(100, 3))

math.sqrt(96)

for i in range(30):
    print(mysqrt)


