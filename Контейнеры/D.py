class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)

    def front(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def clear(self):
        self.queue = []


queue = Queue()

while True:
    command = input().split()
    if command[0] == 'push':
        queue.push(int(command[1]))
        print('ok')
    elif command[0] == 'pop':
        if queue.is_empty():
            print('error')
        else:
            print(queue.pop())
    elif command[0] == 'front':
        if queue.is_empty():
            print('error')
        else:
            print(queue.front())
    elif command[0] == 'size':
        print(queue.size())
    elif command[0] == 'clear':
        queue.clear()
        print('ok')
    elif command[0] == 'exit':
        break

print('bye')
