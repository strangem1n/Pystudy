import sys
dwarfs = list(map(int, sys.stdin.read().splitlines()))
fakes = sum(dwarfs) - 100
checker = False

for i in dwarfs:
    for j in dwarfs:
        if i == j:
            pass
        else:
            if i + j == fakes:
                checker = True
                break
    if checker == True:
        break

dwarfs.remove(i)
dwarfs.remove(j)

dwarfs.sort()
for dwarf in dwarfs:
    print(dwarf)