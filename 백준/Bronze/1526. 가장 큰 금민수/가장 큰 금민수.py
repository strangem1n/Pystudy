def chk(num):
    if num < 10:
        if num == 4 or num == 7:
            return True
        else:
            return False
    else:
        chk_num = num % 10
        next_num = num // 10
        if chk_num == 4 or chk_num == 7:
            return chk(next_num)
        else:
            return False


n = int(input())
while chk(n) is False:
    n -= 1
print(n)
