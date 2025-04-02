T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    result = 0
    for i in range(n, m+1):
        chk = str(i)
        for j in range(len(chk)):
            if chk[j] == "0":
                result += 1
    print(result)
