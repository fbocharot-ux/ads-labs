def counting_sort(arr):

    min_val = min(arr)
    max_val = max(arr)
    count = [0] * (max_val - min_val + 1)

    for x in arr:
        count[x - min_val] += 1

    index = 0
    for i, c in enumerate(count):
        for _ in range(c):
            arr[index] = min_val + i
            index += 1

    return arr

arr = list(map(int, input().split()))
print(*counting_sort(arr))