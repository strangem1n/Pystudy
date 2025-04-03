import math


N = int(input())
arr = list(map(int, input().split()))
prime = set()
for num in arr:
    for chk in range(2, int(math.sqrt(num)+1)):
        if num % chk == 0:
            break
    else:
        prime.add(num)
if len(prime) == 0:
    print(-1)
else:
    result = 1
    for p in prime:
        result *= p
    print(result)
