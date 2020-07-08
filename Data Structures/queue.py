#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 08:44:40 2020

@author: praveen
"""

queue = [] 

queue.append('a')
queue.append('b')
queue.append('c')

print(queue)

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print(queue)


from collections import deque 

q = deque() 
q.append('a') 
q.append('b') 
q.append('c') 
print(q) 

print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q)


from queue import Queue

q = Queue()

q.put('a')
q.put('b')
q.put('c')

print(q.qsize()) 

print(q.get())
print(q.get())
print(q.get())

print(q.qsize()) 

print(q.full())
