import sys


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

    def size(self):
        if self.root is None:
            return 0
        count = 0
        vertexes = [self.root]
        while vertexes:
            count += len(vertexes)
            next_vertexes = []
            for ver in vertexes:
                if ver.left:
                    next_vertexes.append(ver.left)
                if ver.right:
                    next_vertexes.append(ver.right)
            vertexes = next_vertexes
        return count


bst = BinarySearchTree()
numbers = sys.stdin.read().split()
for el in numbers:
    if el != "0":
        bst.insert(int(el))
    else:
        break
print(bst.size())
