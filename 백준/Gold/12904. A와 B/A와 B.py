s = input()
t = input()

for _ in range(len(t)-len(s)):
    t = t[:-1] if t[-1] == 'A' else t[:-1][::-1]

print(1) if s == t else print(0)
