di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def solution(n):
    answer = [[0] * n for _ in range(n)]
    i = 0
    j = -1
    k = 0
    num = 1
    while num <= n**2:
        i += di[k]
        j += dj[k]
        if 0 <= i < n and 0 <= j < n and answer[i][j] == 0:
            answer[i][j] = num
            num += 1
        else:
            i -= di[k]
            j -= dj[k]
            k = (k+1)%4
    return answer