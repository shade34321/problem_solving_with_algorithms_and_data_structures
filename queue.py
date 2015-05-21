#!/usr/bin/env python

class Queue:
    
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.insert(0,data)

    def isEmpty(self):
        return self.items == []

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotPotato(namelist, num):
    
    simpleq = Queue()

    for person in namelist:
        simpleq.enqueue(person)
    
    while simpleq.size() != 1:
        for i in range(num):
            simpleq.enqueue(simpleq.dequeue())

        simpleq.dequeue()

    print"%s won!" % simpleq.dequeue()


names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]

hotPotato(names, 7)
