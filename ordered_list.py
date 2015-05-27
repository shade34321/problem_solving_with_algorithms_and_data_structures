#!/usr/bin/env python

import random

from lists import Lists
from node import Node

class OrderedList(Lists):

    def __init__(self):
        Lists.__init__(self)

    def add(self, item):
        new_node = Node(item)
        temp = self.head
        inserted = False
        prev = None        

        while temp and not inserted:
            if item < temp.getData():
                inserted = True
            else:
                prev = temp
                temp = temp.getNext()

        new_node.setNext(temp)
        
        if not prev:
            self.head = new_node
        else:
            prev.setNext(new_node)
                
    def remove(self, item):
        temp = self.head
        prev = None
        found = False

        while temp and not found:
           if temp.getData() == item:
                found = True
           else:
               prev = temp
               temp = temp.getNext()

        if not prev:
            prev = temp
            self.head = temp.getNext()
        else:
            prev.setNext(temp.getNext())

    def search(self, item):
        temp = self.head
        found = False
        stop = False
        while temp and not found and not stop:
            if temp.getData() == item:
                found = True
            elif temp.getData > item:
                stop = True
            else:
                temp = temp.getNext()

        return found

    def isEmpty(self):
        return self.head == None;

    def size(self):
        temp = self.head
        i = 0

        while temp:
            i += 1
            temp = temp.getNext()

        return i

    def index(self, item):
        temp = self.head
        found = False
        index = 0

        while temp and not found:
            if temp.getData() == item:
                found = True
            else:
                index += 1
                temp = temp.getNext()

        return index
    
    def pop(self, position=-1):
        temp = self.head
        prev = None

        if position == -1 or position == self.size():
            while temp.getNext():
                prev = temp
                temp = temp.getNext()
            
            prev.setNext(None)
        elif position == 1:
            prev = temp.getNext()
            self.head = prev
        else:
            for i in range(position - 1):
                prev = temp
                temp = temp.getNext()
            
            prev.setNext(temp.getNext())

        return temp.getData()

test_list = OrderedList()

print "List size"
print(test_list.size())

print "list isempty"
print(test_list.isEmpty())

print "Adding to list"
for i in range(10):
    x = random.randrange(0,1000)
    test_list.add(x)

test_list.print_list()

test_list.add(8)

print "List size"
print(test_list.size())

print "List Search 8"
print(test_list.search(8))

x = random.randrange(0,1000)
print "List add %d" % x
test_list.add(x)
test_list.print_list()

x = random.randrange(0,1000)
print "List add %d" % x
test_list.add(x)
test_list.print_list()


print "List index 8"
print(test_list.index(8))

print "List remove 8"
test_list.remove(8)
test_list.print_list()

print "List pop"
print (test_list.pop())
test_list.print_list()

print "List pop 3"
print (test_list.pop(3))
test_list.print_list()

print "List pop 1"
print (test_list.pop(1))
test_list.print_list()
