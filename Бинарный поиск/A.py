def binary_searh(arr,find_elem):
    left=0
    right=len(arr)-1
    while left<=right:
        median=(left+right)//2
        if arr[median]==find_elem:
            return True
        elif arr[median]<find_elem:
            left=median+1
        else:
            right=median-1
    return False

N, K = map(int, input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
for i in range(K):
    if binary_searh(arr1,arr2[i]):
        print('YES')
    else:
        print('NO')
