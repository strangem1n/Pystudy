def quicksort(arr, left, right):
    if left < right:
        s = hoare(arr, left, right)
        quicksort(arr, left, s-1)
        quicksort(arr, s+1, right)


def hoare(arr, left, right):
    pivot = arr[left]    # 가장 왼쪽 원소를 피봇으로 정하기
    i = left    # i <= j인 동안 (교차하기 전까지)피봇보다 큰 값을 찾아 오른쪽으로 이동
    j = right    # 피봇보다 작은 값을 찾아 왼쪽으로 이동
    while i <= j:    # 교차하기 전까지
        while i <= j and pivot >= arr[i]:
            i += 1
        while i <= j and pivot <= arr[j]:
            j -= 1
        if i < j:    # 피봇보다 큰 값 오른쪽에 피봇보다 작은 값이 있으면 맞바꾸기
            arr[i], arr[j] = arr[j], arr[i]
    # i, j가 교차한 경우
    # 피봇보다 작은 값 중 가장 오른쪽 위치에 (가장 작은 값x)
    arr[left], arr[j] = arr[j], arr[left]
    return j    # 피봇이 자리잡은 위치 리턴


arr = list(map(int, input().split()))
quicksort(arr, 0, 999999)
print(arr[500000])