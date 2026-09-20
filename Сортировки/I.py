from collections import Counter

str1 = input()
str2 = input()

if Counter(str1) == Counter(str2):
    print("YES")
else:
    print("NO")