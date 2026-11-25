class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        curr_node = self.root
        while True:
            if key < curr_node.data:
                if curr_node.left is None:
                    curr_node.left = Node(key)
                    break
                curr_node = curr_node.left
            elif key > curr_node.data:
                if curr_node.right is None:
                    curr_node.right = Node(key)
                    break
                curr_node = curr_node.right
            else:
                break

    def next_element(self, key):
        curr_node = self.root
        ans = -1
        while curr_node is not None:
            if curr_node.data == key:
                return curr_node.data
            if key < curr_node.data:
                ans = curr_node.data
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return ans


n = int(input())
bst = BinarySearchTree()
out = []
last_y = None

for _ in range(n):
    op, x_str = input().split()
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
    print("\n".join(out))
