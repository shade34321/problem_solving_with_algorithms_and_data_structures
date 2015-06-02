#!/usr/bin/env python

import operator

from binaryTree import BinaryTree
from stack import Stack

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in [ '+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError

    return eTree

def evaluate(pTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = pTree.getLeftChild()
    rightC = pTree.getRightChild()

    if leftC and rightC:
        fn = opers[pTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return pTree.getRootVal()

def postOrderEval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    
    res1 = None
    res2 = None

    if tree:
        res1 = postOrderEval(tree.getLeftChild())
        res2 = postOrderEval(tree.getRightChild())

        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()

def printExp(tree):
    sVal = ""
    
    if tree:
        sVal = "(" + printExp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printExp(tree.getRightChild()) + ')'

    return sVal

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print "Evaluate"
print(evaluate(pt))
print "Postorder"
print(pt.postorder())
print "Preorder"
print(pt.preorder())
print "Inorder"
print(pt.inorder())
print(postOrderEval(pt))
print(printExp(pt))
