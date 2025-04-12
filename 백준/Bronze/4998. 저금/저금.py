import sys
tc = sys.stdin.read().split()

for i in range(0, len(tc), 3):
    n, m, b = float(tc[i]), float(tc[i+1]), float(tc[i+2])
    interest = 1 + m/100
    year = 0
    while n <= b:
        n *= interest
        year += 1
    print(year)
