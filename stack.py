#!/usr/bin/env python

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        if not self.items:
            return True
        else:
            return False

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            elif symbol in ")}]":
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches( first, second):
    openings="({["
    closings=")}]"
    return openings.index(first) == closings.index(second)

def check_parChecker():
    print (parChecker('((()))'))
    print (parChecker('(()'))
    print(parChecker('{{([][])}()}'))
    print(parChecker('[{()]'))
    print (parChecker('(4+x) + ((x-3)+2))'))

def decimal_to_base(number, base):
    rem = 0
    s = Stack()

    while number > 0:
        rem = number % base
        s.push(rem)
        number = number // base
        

    binString = ""
    while not s.isEmpty():
        binString = binString + str(s.pop())

    return binString

def check_int_to_binary():
    print(decimal_to_base(42,2))
    print(decimal_to_base(21,2))
    print(decimal_to_base(512,2))
    print(decimal_to_base(25,2))
    print(decimal_to_base(25,16))
    print(decimal_to_base(25,8))
    print(decimal_to_base(256,16))
    print(decimal_to_base(26,26))
    
check_int_to_binary()
