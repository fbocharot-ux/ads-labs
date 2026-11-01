n = int(input())
train = list(map(int, input().split()))
stack = []
next_number = 1

for vag in train:
    stack.append(vag)
    while stack and stack[-1] == next_number:
        stack.pop()
        next_number += 1

if len(stack) == 0:
    print('YES')
else:
    print('NO')
