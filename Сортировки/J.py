from functools import cmp_to_key
import sys

def cmp_pieces(a, b):
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0



arr= sys.stdin.read().split()
arr.sort(key=cmp_to_key(cmp_pieces))
print("".join(arr))