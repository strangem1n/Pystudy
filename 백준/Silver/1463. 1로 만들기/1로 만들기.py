def f(n):
    if n == 1:
        return 0
    else:
        visited = [0] * (n+1)
        visited[1] = 1

        arr = [[1]]
        cnt = 0
        while True:
            cnt += 1
            subset = []
            for a in arr:
                for b in a:
                    triple = b * 3
                    if triple == n:
                        return cnt
                    elif triple < n and visited[triple] == 0:
                        subset.append(triple)
                        visited[triple] = 1

                    double = b * 2
                    if double == n:
                        return cnt
                    elif double < n and visited[double] == 0:
                        subset.append(double)
                        visited[double] = 1

                    plus_one = b + 1
                    if plus_one == n:
                        return cnt
                    elif visited[plus_one] == 0:
                        subset.append(plus_one)
                        visited[plus_one] = 1
            arr.append(subset)


num = int(input())
print(f(num))
