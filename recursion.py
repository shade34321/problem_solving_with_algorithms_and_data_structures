#!/usr/bin/env python

import string

def reverse(data):
    if len(data) <= 1:
        return data
    else:
        return data[-1] + reverse(data[:-1])

def removeWhite(data):
    data.translate(None, string.punctuation)
    return "".join(data.split())

def isPal(data):
    tester = removeWhite(data)
    print "Tester: %s" % tester
    tester = reverse(tester)
    print "Tester: %s" % tester
    return removeWhite(data.lower()) == tester.lower() 

print "Passing test"
print(reverse("test"))

print(isPal("madam"))
test_str = "Live not on evil"
print "Checking if %s is a palindrome: %r" % (test_str, isPal(test_str))
test_str = "Go hang a salami; I.m a lasagna hog."
print "Checking if %s is a palindrome: %r" % (test_str, isPal(test_str))
