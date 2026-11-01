h = list(map(int, input().split()))
n = h.pop(0)
h.append(0)
stack = []
max_area = 0

for i in range(len(h)):
    while stack and h[i] < h[stack[-1]]:
        height_idx = stack.pop()
        current_height = h[height_idx]
        if not stack:
            width = i
        else:
            width = i - stack[-1] - 1
        current_area = current_height * width
        if current_area > max_area:
            max_area = current_area
    stack.append(i)

print(max_area)
