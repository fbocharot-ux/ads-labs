


def first_index(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


def last_index(arr, x):

    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left



N = int( input())
arr1 = list(map(int, input().split()))
K = int(input())
arr2 = list(map(int, input().split()))
arr1.sort()
res=[]
for x in arr2:
    count = last_index(arr1, x) - first_index(arr1, x)
    res.append(count)
print(*res)

