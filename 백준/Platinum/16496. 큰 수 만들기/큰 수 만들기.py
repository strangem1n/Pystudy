import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().split())
arr.sort(key=lambda x: x*10, reverse=True)
result = ''.join(arr)
if result[0] == '0':
    print(0)
else:
    print(result)
