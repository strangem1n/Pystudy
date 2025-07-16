import sys

def div(num):
    if num <= 1:
        return 2 ** num
    else:
        if num % 2 == 0:
            return (div(num//2) ** 2) % (10**9+7)
        else:
            return (div(num//2) ** 2 * 2) % (10**9+7)

n = int(sys.stdin.readline())
if n == 0:
    print(1)
else:
    print(div(n-1))