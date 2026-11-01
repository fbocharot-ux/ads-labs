balls = list(map(int, input().split()))
count = 0

while True:
    found_sequence = False
    i = 0

    while i < len(balls):
        j = i
        while j < len(balls) and balls[j] == balls[i]:
            j += 1

        length = j - i
        if length >= 3:
            count += length
            balls = balls[:i] + balls[j:]
            found_sequence = True
            break

        i = j

    if not found_sequence:
        break

print(count)
