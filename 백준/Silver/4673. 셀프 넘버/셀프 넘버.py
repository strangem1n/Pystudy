def d(n):
    if n < 10:
        return n
    else:
        return n%10 + d(n//10)
    
arr = [0] * 10001
for i in range(1, 10001):
    if 0 < i+d(i) < 10001:
        arr[i+d(i)] = 1
        
for j in range(1, 10001):
    if arr[j] == 0:
        print(j)
