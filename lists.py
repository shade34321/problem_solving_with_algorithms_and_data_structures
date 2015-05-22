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
                temp = temp.getNext

            temp.setNext(new_node)
        
    
    def insert(self, pos, data):
        new_node = Node(data)
        temp = self.head

        for i in range(pos):
            temp = temp.getNext()

        new_node.setNext(temp.getNext())
        temp.setNext(new_node)

    def print_list(self):
        temp = self.head
        str_list = ""

        while temp != None:
            str_list = str(temp.getData()) + " -> "
            temp = temp.getNext()

        print "%s%d" % (str_list, temp.getData())

    #def index(self):

    #def pop(self):



test_list = UnorderedList()

for i in range(10):
    test_list.add(i)

test_list.print_list()
