s = int(input())

i = 0
total = 0
while total < s:
    i += 1
    total += i
if total == s:
    print(i)
else:
    print(i-1)