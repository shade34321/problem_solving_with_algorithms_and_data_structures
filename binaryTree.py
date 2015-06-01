#!/usr/bin/env python

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.rightChild = self.rightChild
            self.rightChild = temp

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, data):
        self.key = data

    def getRootVal(self):
        return self.key

def buildTree():
    bt = BinaryTree('a')
    bt.insertLeft('b')
    bt.insertRight('c')
    bt.getLeftChild().insertRight('d')
    bt.getRightChild().insertLeft('e')
    bt.getRightChild().insertRight('f')

    return bt
