n = int(input())
a = list(map(int, input().split()))
pref = [0] * (n + 1)

for i in range(n):
    pref[i + 1] = pref[i] + a[i]

stack = []
max_sig = -1
best_l = 1
best_r = 1

a.append(-1)

for i in range(n + 1):
    while stack and a[i] < a[stack[-1]]:
        idx = stack.pop()
        min_val = a[idx]

        right = i - 1
        left = stack[-1] + 1 if stack else 0
        current_sum = pref[right + 1] - pref[left]
        current_sig = min_val * current_sum

        if current_sig > max_sig:
            max_sig = current_sig
            best_l = left + 1
            best_r = right + 1

    stack.append(i)

print(max_sig)
print(f"{best_l} {best_r}")
