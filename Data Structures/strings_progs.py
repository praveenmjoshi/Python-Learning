#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:23:34 2020

@author: praveen
"""

'''
    Logical programs on strings

'''

def find_duplicates(msg):
    temp = {}
    for ch in msg:
        if ch in temp.keys(): 
            temp[ch] += 1
        else:
            temp[ch] = 1
    
    dups = [val for val in temp if temp[val] > 1]
    print(dups)
    
msg = 'hello world'
find_duplicates(msg)


def check_anagram(str1, str2):
    msg = 'Yes Anagram'
    if len(str1) != len(str2):
        msg = "Not anagram"
    
    str1 = sorted(str1)
    str2 = sorted(str2)
    
    print(str1, str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            msg = 'Not anagram'
            break;
    
    print(msg)

    

str1 = 'xys'
str2 = 'sxy'
check_anagram(str1,str2)

def find_unique(msg):
    
    chars = {}
    for i in msg:
        if i.lower() in chars.keys():
            chars[i.lower()] += 1
        else:
            chars[i.lower()] = 0
    print(chars)
    
    for val in chars:
        if chars[val] == 0:
            print(val)
            break;


str1 = 'GeeksForGeeks'
find_unique(str1)


def reverse_str(msg):
    msg = msg[::-1]
    print(msg.lower())
    
str1 = 'I am Good'
reverse_str(str1)
    

def count_vowels(str1):
    vowels_count = {}
    
    for i in 'aeiou':
        count = str1.count(i)
        if count > 0 :
            vowels_count[i] = count
    print(vowels_count)
    
    print(sum(vowels_count.values()))
    
a = 'abcdefe'
count_vowels(a)



def check_palindrom(str1):
    
    msg = 'Yes Palindrome'
    for i in range(int(len(str1)/2)):
        if str1[i] != str1[-1-i]:
            msg = 'Not Palindrome'
            break
    print(msg)
    
str1 =  'GADAG'
check_palindrom(str1)


class A:
   
    def __change(self):
        return 10
    def disp(self):
        print(self.__change())

class B(A):
    def __change(self):
        return 5
        

ob = A()
ob.disp()

ob1 = B()
ob1.disp()