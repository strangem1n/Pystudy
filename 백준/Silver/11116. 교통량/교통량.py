import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))

    result = 0
    for time in left:
        if time+500 in left and time+1000 in right and time+1500 in right:
            result += 1
    print(result)
