from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

subset = permutations(arr, m)
result = []
for i in subset:
    result.append(i)
result = list(set(result))
result.sort()
for r in result:
    print(*r)
