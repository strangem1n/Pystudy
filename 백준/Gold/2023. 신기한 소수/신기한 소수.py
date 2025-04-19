import math

def chk(num):
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True

def f(num, cnt):
    if cnt == n-1:
        print(num)

    else:
        num *= 10
        for i in [1, 3, 7, 9]:
            test_num = num + i
            if chk(test_num):
                f(test_num, cnt+1)

n = int(input())
for k in [2, 3, 5, 7]:
    f(k, 0)
