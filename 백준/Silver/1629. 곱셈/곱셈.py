import sys
input = sys.stdin.readline

def power(x, y, q):
    if y <= 2:
        return (x ** y) % q
    elif y % 2 == 1:
        return (power(x, y//2, q) * power(x, (y//2)+1, q)) % q
    else:
        return (power(x, y//2, q) ** 2) % q

a, b, c = map(int, input().split())
print(power(a, b, c))
