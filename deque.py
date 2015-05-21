#!/usr/bin/env python

class Deque:
    
    def __init__(self):
       self.items = []

    def addFront(self, data):
        self.items.append(data)

    def addRear(self, data):
        self.items.insert(0,data)
    
    def removeRear(self):
        return self.items.pop()

    def removeFront(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def palindrome(aString):
    charDeque = Deque()
    stillEqual = True

    for ch in aString:
        charDeque.addRear(ch)

    while charDeque.size() > 1 and stillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print palindrome("lsdkjfskf")
print palindrome("radar")
