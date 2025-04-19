import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
charge = list(map(int, input().split()))

total = 0
oil = charge[0]
length = 0
for i in range(1, N):
    length += road[i-1]
    if charge[i] < oil:
        total += oil * length
        oil = charge[i]
        length = 0

total += oil * length
print(total)
