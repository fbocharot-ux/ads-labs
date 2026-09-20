def bubble_sort(arr):
    count_change = 0
    for i in range(len(arr)-1):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
                count_change+=1
        if not swap:
            break
    return count_change

n=int(input())
arr = list(map(int,input().split()))
print(bubble_sort(arr))