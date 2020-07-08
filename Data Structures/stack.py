#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 08:37:50 2020

@author: praveen
"""


'''
    Different ways of stack implementations
'''

stack = [] 

stack.append('a') 
stack.append('b') 
stack.append('c') 

print(stack)


print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 

print(stack) 


# Using deque from collections

from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print(stack) 

print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 

print(stack) 



# Using LifoQueue from queue module

from queue import LifoQueue 

stack = LifoQueue(maxsize = 3)

print(stack.qsize())

stack.put('a') 
stack.put('b') 
stack.put('c') 

print("Full: ", stack.full())  
print("Size: ", stack.qsize())

print(stack.get())
print(stack.get())
print(stack.get())

print("Size: ", stack.qsize())