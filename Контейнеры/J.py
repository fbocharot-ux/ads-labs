N = int(input())
res = []

for _ in range(N):
    data = list(map(float, input().split()))
    k = int(data[0])
    arr = data[1:]
    except_arr = sorted(arr)
    stack = []
    index = 0
    for cont in arr:
        stack.append(cont)
        while stack and stack[-1] == except_arr[index]:
            stack.pop()
            index += 1
    if index == k:
        res.append('1')
    else:
        res.append('0')

print('\n'.join(res))
