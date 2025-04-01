def civilization(city_num, prev_k, sum_w, sum_c, sum_f):
    global min_region

    if city_num > min_region:
        return

    if req_w > sum_w or req_c > sum_c or req_f > sum_f:
        for k in range(prev_k+1, N):
            if used[k] == 0:
                used[k] = 1
                civilization(city_num+1, k, sum_w+w[k], sum_c+c[k], sum_f+f[k])
                used[k] = 0
    else:
        if min_region > city_num:
            min_region = city_num


T = int(input())
for _ in range(T):
    N = int(input())
    req_w, req_c, req_f = map(int, input().split())
    w = [0] * N
    c = [0] * N
    f = [0] * N
    for i in range(N):
        w[i], c[i], f[i] = map(int, input().split())

    if sum(w) < req_w or sum(c) < req_c or sum(f) < req_f:
        print("game over")
    else:
        min_region = N
        used = [0] * N
        civilization(0, -1, 0, 0, 0)
        print(min_region)
