def mergeSort(arr):
    if len(arr)<=1:
        return arr
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        left=mergeSort(left)
        right=mergeSort(right)
        i = j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result.extend(left[i:])
        result.extend(right[j:])
    return result

n = int(input())
arr=list(map(int,input().split()))
print(*mergeSort(arr))
