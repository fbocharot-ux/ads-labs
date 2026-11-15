import sys


class BinarySearchTree:

    def __init__(self):
        self.data = []
        self.left = []
        self.right = []

    def insert(self, key):
        if not self.data:
            self.data.append(key)
            self.left.append(-1)
            self.right.append(-1)
            return

        curr = 0
        data_arr = self.data
        left_arr = self.left
        right_arr = self.right

        while True:
            d = data_arr[curr]
            if key < d:
                nxt = left_arr[curr]
                if nxt == -1:
                    left_arr[curr] = len(data_arr)
                    data_arr.append(key)
                    left_arr.append(-1)
                    right_arr.append(-1)
                    break
                curr = nxt
            elif key > d:
                nxt = right_arr[curr]
                if nxt == -1:
                    right_arr[curr] = len(data_arr)
                    data_arr.append(key)
                    left_arr.append(-1)
                    right_arr.append(-1)
                    break
                curr = nxt
            else:
                break

    def next_element(self, key):
        if not self.data:
            return -1
        curr = 0
        ans = -1
        data_arr = self.data
        left_arr = self.left
        right_arr = self.right

        while curr != -1:
            d = data_arr[curr]
            if d == key:
                return d
            if key < d:
                ans = d
                curr = left_arr[curr]
            else:
                curr = right_arr[curr]
        return ans


first_line = sys.stdin.readline()
if first_line:
    n = int(first_line)
    bst = BinarySearchTree()
    out = []
    last_y = None

    for _ in range(n):
        op, x_str = sys.stdin.readline().split()
        x = int(x_str)
        if op == "+":
            if last_y is not None:
                x = (x + last_y) % 1000000000
            bst.insert(x)
            last_y = None
        else:
            y = bst.next_element(x)
            out.append(str(y))
            last_y = y

    if out:
        sys.stdout.write("\n".join(out) + "\n")