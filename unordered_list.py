#!/usr/bin/env python

class Node:
    
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, next_node):
        self.next = next_node

class UnorderedList:
    
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def size(self):
        temp = self.head
        list_size = 0

        while temp != None:
            list_size = list_size + 1
            temp = temp.getNext()

        return list_size

    def search(self, data):
        temp = self.head
        found = False

        while temp != None and not found:
            if temp.getData() == data:
                found = True
            else:
                temp = temp.getNext()

        return found

        
    def remove(self, data):
        temp = self.head
        previoius = None
        found = False
    
        while not found:
            if temp.getData() == data:
                found = True
            else:
                previous = temp
                temp = temp.getNext()

        if previous == None:
            self.head = temp.getNext()
        else:
            previous.setNext(temp.getNext())

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

    def print_list(self):
        temp = self.head
        str_list = ""

        while temp.getNext() != None:
            str_list += str(temp.getData()) + " -> "
            temp = temp.getNext()

        print "%s%d" % (str_list, temp.getData())

    def index(self, data):
        temp = self.head
        found = False
        i = 0

        while temp != None and not found:
            if temp.getData() == data:
                found = True
            else:
                i += 1
                temp = temp.getNext()

        return i
    
    def pop(self):
        temp = self.head
        prev = None

        while temp.getNext() != None:
            prev = temp
            temp = temp.getNext()

        data = temp.getData()
        prev.setNext(None)
        return data
    
    def pop(self, pos):
        temp = self.head
        prev = None
      
        if pos == 0:
            temp = temp.getNext()
            self.head = temp 
            data = temp.getData()
        else: 
            for i in range(pos):
                prev = temp
                temp = temp.getNext()

            prev.setNext(temp.getNext())
            data = temp.getData()

        return data
        

test_list = UnorderedList()

print "List size"
print(test_list.size())

print "Adding to list"
for i in range(10):
    test_list.add(i)

print "List size"
print(test_list.size())

print "List Search"
print(test_list.search(8))

print "List insert"
test_list.insert(2,11)
test_list.print_list()

print "List append"
test_list.append(12)
test_list.print_list()

print "List remove"
test_list.remove(8)
test_list.print_list()

print "List index"
print(test_list.index(4))

print "List pop"
print (test_list.pop(3))
