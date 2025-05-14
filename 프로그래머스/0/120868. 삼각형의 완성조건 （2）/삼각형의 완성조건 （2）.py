def solution(sides):
    a, b = sides
    c = 0
    answer = 0
    while True:
        c += 1
        longest = max(a, b, c)
        if longest < a + b + c - longest:
            answer += 1
        else:
            if longest == c:
                return answer