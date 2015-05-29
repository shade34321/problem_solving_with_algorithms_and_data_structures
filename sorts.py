#!/usr/bin/env python

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1], alist[i]

def shortBubble(alist):
    exchange = True
    passnum = len(alist)-1

    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]

        passnum = passnum - 1

def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        max = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[max] and location != max:
                max = location

        alist[fillslot],alist[max] = alist[max], alist[fillslot]

def insertionSort(alist):
    for i in range(1,len(alist)):
        cv = alist[i]
        position = i
        
        while position > 0 and alist[position-1] > cv:
            alist[position] = alist[position-1]
            position = position - 1
    
        alist[position] = cv

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

def mergeSort(alist):
   if len(alist) > 1:
    mid = len(alist)//2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]

    mergeSort(lefthalf)
    mergeSort(righthalf)

    i = 0
    j = 0
    k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[k] = lefthalf[i]
            i = i + 1
        else:
            alist[k] = righthalf[j]
            j = j + 1
    
        k = k + 1

    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i = i + 1
        k = k + 1

    while j < len(righthalf):
        alist[k] = righthalf[j]
        j = j + 1
        k = k + 1

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)

def partition(alist, first, last):
    pivotvalue = alist[first]
    
    leftmark = first + 1
    rightmark = last

    done = False
    
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark  - 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

alist = [54,26,93,17,77,31,44,55,20]
shortBubble(alist)
print(alist)

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
