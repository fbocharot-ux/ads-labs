
class Node:
    __slots__ = ("data", "count", "left", "right")

    def __init__(self, key):
        self.data = key
        self.count = 1
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
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
                    curr_node.count += 1
                    break

    def order_up(self):
        result = []
        self._order_up(self.root, result)
        return result

    def _order_up(self, node, result):
        if node is None:
            return
        self._order_up(node.left, result)
        result.append(f"{node.data} {node.count}")
        self._order_up(node.right, result)


bst = BinarySearchTree()
numbers = input().split()
for el in numbers:
    if el != "0":
        bst.insert(int(el))
    else:
        break
print(*bst.order_up(), sep="\n")