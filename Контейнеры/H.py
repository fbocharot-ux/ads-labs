from collections import deque

left = deque()
right = deque()


def balance():
    if len(right) > len(left):
        left.append(right.popleft())


n = int(input())
res = []

for i in range(n):
    command = list(input().split())
    if command[0] == '+':
        right.append(int(command[1]))
        balance()
    elif command[0] == '*':
        right.appendleft(int(command[1]))
        balance()
    elif command[0] == '-':
        res.append(left.popleft())
        balance()

print('\n'.join(map(str, res)))
