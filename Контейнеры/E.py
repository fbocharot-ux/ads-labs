class Deque:
    def __init__(self):
        self.items = []

    def push_back(self, item):
        self.items.append(item)

    def push_front(self, item):
        self.items.insert(0, item)

    def pop_front(self):
        return self.items.pop(0)

    def pop_back(self):
        return self.items.pop()

    def front(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def back(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()


deca = Deque()

while True:
    command = input().split()
    if command[0] == 'push_back':
        deca.push_back(command[1])
        print('ok')
    elif command[0] == 'push_front':
        deca.push_front(command[1])
        print('ok')
    elif command[0] == 'pop_front':
        if deca.is_empty():
            print('error')
        else:
            print(deca.pop_front())
    elif command[0] == 'pop_back':
        if deca.is_empty():
            print('error')
        else:
            print(deca.pop_back())
    elif command[0] == 'front':
        if deca.is_empty():
            print('error')
        else:
            print(deca.front())
    elif command[0] == 'back':
        if deca.is_empty():
            print('error')
        else:
            print(deca.back())
    elif command[0] == 'size':
        print(deca.size())
    elif command[0] == 'clear':
        deca.clear()
        print('ok')
    elif command[0] == 'exit':
        break

print('bye')
