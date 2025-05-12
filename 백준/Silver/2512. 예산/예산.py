import sys
input = sys.stdin.readline

def solve(max_budget):
    left = 0
    right = max_budget
    while left <= right:
        middle = (left + right) // 2
        temp = 0
        for i in range(n):
            if arr[i] <= middle:
                temp += arr[i]
            else:
                temp += middle
        if temp == budget:
            return middle
        elif temp > budget:
            right = middle - 1
        else:
            left = middle + 1
    if temp > budget:
        return middle - 1
    else:
        return middle

n = int(input())
arr = list(map(int, input().split()))
budget = int(input())

print(solve(max(arr)))