stroka = input()
stack = []
ans = True

for char in stroka:
    if char not in ['{', '[', '(', '}', ']', ')']:
        continue
    if char in ['{', '[', '(']:
        stack.append(char)
        continue
    if len(stack) != 0 and (
        char == '}' and stack[-1] == '{' or
        char == ')' and stack[-1] == '(' or
        char == ']' and stack[-1] == '['
    ):
        stack.pop()
    else:
        ans = False
        break

if len(stack) != 0:
    ans = False

print('yes' if ans else 'no')
