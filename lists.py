#!/usr/bin/env python

class Lists:
    
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

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
        previous = None
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
    
    def print_list(self):
        temp = self.head
        ordered_list = ""

        while temp.getNext():
            ordered_list += str(temp.getData()) + " -> "
            temp = temp.getNext()

        ordered_list += str(temp.getData())
        print ordered_list
    
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
    
    def pop(self, pos=-1):
        temp = self.head
        prev = None

        if pos == -1 or pos == self.size():
            while temp.getNext():
                prev = temp
                temp = temp.getNext()

            prev.setNext(None)
        elif pos == 1:
            prev = temp.getNext()
            self.head = prev
        else:
            for i in range(pos - 1):
                prev = temp
                temp = temp.getNext()
            prev.setNext(temp.getNext())
        
        data = temp.getData()

        return data
