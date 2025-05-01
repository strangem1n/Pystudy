while True:
    n, *nums = map(int, input().split())
    if n == 0:
        break

    nums.sort()
    if nums[0] == 0:
        for i in range(1, n):
            if nums[i] != 0:
                nums[i], nums[0] = nums[0], nums[i]
                nums[i+1], nums[1] = nums[1], nums[i+1]
                break

    num1 = [0] * (n//2+1) if n % 2 == 1 else [0] * (n//2)
    num2 = [0] * (n//2)

    for i in range(n):
        if i % 2 == 0:
            num1[i//2] = nums[i]
        else:
            num2[i//2] = nums[i]

    a = int(''.join(map(lambda x: str(x), num1)))
    b = int(''.join(map(lambda x: str(x), num2)))
    print(a+b)
