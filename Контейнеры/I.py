balls = list(map(int, input().split()))
stack = []
count = 0

for color in balls:
    if not stack:
        stack.append([color, 1])
    else:
        if stack[-1][0] == color:
            stack[-1][1] += 1
        else:
            if stack[-1][1] >= 3:
                count += stack[-1][1]
                stack.pop()
                if stack and stack[-1][0] == color:
                    stack[-1][1] += 1
                else:
                    stack.append([color, 1])
            else:
                stack.append([color, 1])

if stack and stack[-1][1] >= 3:
    count += stack[-1][1]
    stack.pop()

print(count)
