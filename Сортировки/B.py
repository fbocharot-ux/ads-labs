def InsertionSort(arr):
    for i in range(1, len(arr)):
        elem=arr[i]
        index=i-1
        while index>=0 and arr[index]>elem:
            arr[index+1]=arr[index]
            index=index-1
        arr[index+1]=elem
arr=list(map(int,input().split()))
InsertionSort(arr)
print(*arr)



