import math


def turn(a, b):
    r = math.atan2(b, a)
    return round(math.degrees(r))


while True:
    x, y = map(int, input().split())
    if x == y == 0:
        break
    print(turn(x, y))
