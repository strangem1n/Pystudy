n = int(input())
m = int(input())
string = input()

chk = "I" + ("OI" * n)
cnt = 0
for i in range(m-2*n):
    if chk == string[i:i+(2*n+1)]:
        cnt += 1
print(cnt)