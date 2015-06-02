#!/usr/bin/env python

class BinHeap:
    
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]

            i = i // 2
    
    def delMin(self):
        min = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return min

    def percDown(self, i):
        while (i*2) <= self.currentSize:
            min = self.minChild(i)
            if self.heapList[i] > self.heapList[min]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[min]
                self.heapList[min] =  tmp

            i = min
    
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def isEmpty(self):
        return self.size == 0
    
    def size(self):
        return self.size

    def buildHeap(self, key_list):
        i = len(key_list) // 2
        self.currentSize = len(key_list)
        self.heapList = [0] + key_list[:]
        while (i > 0):
            self.percDown(i)
            i -= 1

bh = BinHeap()
#bh.insert(5)
#bh.insert(7)
#bh.insert(3)
#bh.insert(11)

#print(bh.delMin())
#print(bh.delMin())
#print(bh.delMin())
#print(bh.delMin())

print "List adding"

bh.buildHeap([9,5,6,2,3])
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())

