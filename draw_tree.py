#!/usr/bin/env python

import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(10)
        tree(branchLen-5,t)
        t.left(20)
        tree(branchLen-5,t)
        t.right(10)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(15)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()
