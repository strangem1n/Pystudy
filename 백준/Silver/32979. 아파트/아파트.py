n = int(input())
t = int(input())
arr = list(map(int, input().split()))
game = list(map(int, input().split()))

result = [0] * t
idx = 0
for i in range(t):
    idx = (idx + game[i] - 1) % (2 * n)
    result[i] = arr[idx]
print(*result)
