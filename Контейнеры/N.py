from collections import deque

p1 = deque(map(int, input().split()))
p2 = deque(map(int, input().split()))

moves = 0
limit = 1000000

while p1 and p2 and moves < limit:
    c1 = p1.popleft()
    c2 = p2.popleft()

    if c1 == 0 and c2 == 9:
        winner = 1
    elif c1 == 9 and c2 == 0:
        winner = 2
    elif c1 > c2:
        winner = 1
    else:
        winner = 2

    if winner == 1:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c1)
        p2.append(c2)

    moves += 1

if not p1:
    print(f"second {moves}")
elif not p2:
    print(f"first {moves}")
else:
    print("botva")
