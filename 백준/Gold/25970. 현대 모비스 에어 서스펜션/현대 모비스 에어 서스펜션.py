import sys
input = sys.stdin.readline

b = int(input())
test = [None] * (2 * b)
for i in range(b):
    test[i] = input().rstrip()
for i in range(b, 2*b):
    test[i] = input().rstrip()

n = int(input())
for _ in range(n):
    data = input().rstrip()
    c = 0
    for i in range(len(data)):
        for t in range(2*b):
            try:
                if data[i:i+len(test[t])] == test[t]:
                    if t < b:
                        c -= 1
                    else:
                        c += 1
            except:
                continue

    if c > 0:
        print(f"LOW {c}")
    elif c == 0:
        print("GOOD")
    else:
        print(f"HIGH {-c}")
