stroka = input().split()
stack = []

for char in stroka:
    if not char.isnumeric():
        b = stack.pop()
        a = stack.pop()
        if char == '+':
            stack.append(a + b)
        if char == '-':
            stack.append(a - b)
        if char == '*':
            stack.append(a * b)
        if char == '/':
            stack.append(a / b)
    else:
        stack.append(int(char))

print(stack[0])
