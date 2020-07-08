#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:29:53 2020

@author: praveen
"""


'''
    Logical programs on arrays

'''


def search_missing(arr):
    n = len(arr) + 1
    total = (n)*(n+1)/2
    sum_of_arr = sum(arr)
    print( int(total - sum_of_arr ))
    

arr = [1,2,3,4,6,7,8]
search_missing(arr)


def find_duplicate(arr):
    
    for i in range(0, len(arr)):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            pass
            print( abs(arr[i]) , end = ' ')
            

def find_largest(arr):
    number = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > number:
            number = arr[i]
        
    print(number)
    
      
def find_largest_num(arr):
    print(max(arr))



def find_duplicates(arr):
    temp = []
    temp = [value for index,value in enumerate(arr) if arr.index(value) == index ]
    print(temp)
    
arr = [9,2,8,4,6,7,8]

find_duplicates(arr)