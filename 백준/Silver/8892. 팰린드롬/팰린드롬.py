def chk():
    for i in range(N):
        for j in range(N):
            if i != j:
                word = arr[i] + arr[j]
                if pal(word):
                    return word
    return 0


def pal(w):
    for k in range(len(w)//2):
        if w[k] != w[-(k+1)]:
            return False
    return True


T = int(input())
for _ in range(T):
    N = int(input())
    arr = [input() for __ in range(N)]
    print(chk())
