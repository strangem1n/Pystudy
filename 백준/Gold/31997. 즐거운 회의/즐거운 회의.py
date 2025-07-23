import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
person_in = [0] * (n+1)
person_out = [0] * (n+1)
for i in range(1, n+1):
    person_in[i], person_out[i] = map(int, input().split())

session = [0] * (t+1)
for _ in range(m):
    c, d = map(int, input().split())
    common_initial = max(person_in[c], person_in[d])
    common_terminal = min(person_out[c], person_out[d])
    if common_terminal > common_initial:
        session[common_initial] += 1
        session[common_terminal] -= 1

for i in range(1, t+1):
    session[i] += session[i-1]
for i in range(t):
    print(session[i])