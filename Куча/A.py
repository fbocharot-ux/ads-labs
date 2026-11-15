class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0
    def ShiftUp(self,i):
        while i//2>0 and self.heap[i]>self.heap[i//2]:
            self.heap[i],self.heap[i//2] = self.heap[i//2],self.heap[i]
            i = i//2
    def Insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.ShiftUp(self.size)
    def indMaxChild(self,i):
        if i*2+1>self.size:
            return i*2
        if self.heap[i*2]>self.heap[i*2+1]:
                return i*2
        return i*2+1
    def ShiftDown(self,i):
        while 2*i<=self.size:
            j = self.indMaxChild(i)
            if self.heap[i]<self.heap[j]:
                self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
            i=j
    def Extract(self):
        if self.size==0:
            return None
        removed =self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size = self.size-1
        self.heap.pop()
        self.ShiftDown(1)
        return removed

n=int(input())
heap = Heap()
for i in range(n):
    command = list(map(int,input().split()))
    if command[0]==0:
        heap.Insert(command[1])
    if command[0]==1:
        print(heap.Extract())
