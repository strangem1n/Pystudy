import math
def divisor(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if i == n // i:
                cnt += 1
            else:
                cnt += 2
    return cnt

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if divisor(num) % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer