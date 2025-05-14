import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

dic = {}
if n < m:
    array = sorted(a, reverse=True)
    compare = b
else:
    array = sorted(b, reverse=True)
    compare = a

subset = []
for element in array:
    for com in compare:
        if element == com:
            subset.append(com)
            break

result = []
for element in subset:
    ai = bi = 0
    while ai < len(a) and bi < len(b):
        if element == a[ai] == b[bi]:
            result.append(element)
            a = a[ai+1:]
            b = b[bi+1:]
            break
        elif element == a[ai]:
            bi += 1
        elif element == b[bi]:
            ai += 1
        else:
            ai += 1
            bi += 1

print(len(result))
if result:
    print(*result)
