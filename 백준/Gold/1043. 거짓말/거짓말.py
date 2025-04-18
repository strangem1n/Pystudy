def find_set(x):
    if rep[x] != x:
        rep[x] = find_set(rep[x])
        return rep[x]
    else:
        return x


def union(x, y):
    a = find_set(x)
    b = find_set(y)
    if a < b:
        rep[b] = a
    else:
        rep[a] = b


n, m = map(int, input().split())
know = list(map(int, input().split()))
truth = [False] * (n+1)

if len(know) != 1:
    for i in range(1, know[0]+1):
        truth[know[i]] = True

rep = [i for i in range(n+1)]
party = []
for _ in range(m):
    num, *people = map(int, input().split())
    for i in range(num-1):
        union(people[i], people[i+1])
    party.append(people)

for i in range(n+1):
    if truth[i]:
        for j in range(n+1):
            if rep[find_set(j)] == rep[find_set(i)]:
                truth[j] = True

result = 0
for i in range(len(party)):
    for p in party[i]:
        if truth[find_set(p)]:
            break
    else:
        result += 1
print(result)
