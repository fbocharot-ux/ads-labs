def binary_searh(arr, x):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


N, K = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for x in arr2:
    pos = binary_searh(arr1, x)
    if pos == 0:
        print(arr1[0])
    elif pos == N:
        print(arr1[N - 1])
    else:
        left = arr1[pos - 1]
        right = arr1[pos]
        if x - left <= right - x:
            print(left)
        else:
            print(right)



