#!/usr/bin/env python

from lists import Lists
from node import Node

class UnorderedList(Lists):
    
    def __init__(self):
        Lists.__init__(self)

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def append(self, data):
        new_node = Node(data)
        temp = self.head

        if self.head == None:
            self.head = new_node
        else:
            while temp.getNext() != None:
                temp = temp.getNext()

            temp.setNext(new_node)
        
    
    def insert(self, pos, data):
        new_node = Node(data)
        temp = self.head

        if pos == 0:
            self.add(data)
        elif pos == self.size():
            self.append(data)
        else:         
            for i in range(pos):
                temp = temp.getNext()

            new_node.setNext(temp.getNext())
            temp.setNext(new_node)

test_list = UnorderedList()

print "List size"
print(test_list.size())

print "Adding to list"
for i in range(10):
    test_list.add(i)

print "List size"
print(test_list.size())

print "List Search 8"
print(test_list.search(8))

print "List insert"
test_list.insert(2,11)
test_list.print_list()

print "List append"
test_list.append(12)
test_list.print_list()

print "List remove 8"
test_list.remove(8)
test_list.print_list()

print "List index 5"
print(test_list.index(4))

print "List pop"
print (test_list.pop())
test_list.print_list()

print "List pop 3"
print (test_list.pop(3))
test_list.print_list()

print "List pop 1"
print (test_list.pop(1))
test_list.print_list()
