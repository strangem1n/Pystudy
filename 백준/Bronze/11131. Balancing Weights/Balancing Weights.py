T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    avg = sum(arr)
    if avg == 0:
        print('Equilibrium')
    elif avg > 0:
        print('Right')
    else:
        print('Left')
