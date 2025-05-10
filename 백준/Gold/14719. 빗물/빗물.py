h, w = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
stock = 0
prev = 0
stack = []
for i in range(w):
    if prev <= arr[i]:
        for s in stack:
            arr[s] = min(prev, arr[i])
        prev = arr[i]
        total += stock
        stock = 0
        stack = []
    else:
        stock += prev - arr[i]
        stack.append(i)

stock = 0
prev = 0
for i in range(w-1, -1, -1):
    if prev <= arr[i]:
        prev = arr[i]
        total += stock
        stock = 0
    else:
        stock += prev - arr[i]

print(total)