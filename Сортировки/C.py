def bubble_sort(arr):
    n = len(arr)
    for iteration in range(n - 1):
        swap = False
        for i in range(n - iteration - 1):
            if arr[i] <= arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
        if not swap:
            break


num = list(map(int, input().split()))
bubble_sort(num)
print(*num)