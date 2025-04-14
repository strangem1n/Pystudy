import sys
input = sys.stdin.readline

n, k = map(int, input().split())
hamburger = input().rstrip()
ate = [0] * n
cnt = 0

for i in range(n):
    if hamburger[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0 <= j < n and hamburger[j] == 'H' and ate[j] == 0:
                ate[j] = 1
                cnt += 1
                break
print(cnt)
