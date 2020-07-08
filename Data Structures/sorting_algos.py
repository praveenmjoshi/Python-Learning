# -*- coding: utf-8 -*-

'''
    Bubble sort algorithm
   
'''
def bubble_sort(arr):
    for k in range(len(arr)-1):
        swapped = False
        for i in range(len(arr) - 1):
            #print(i)
            if( arr[i] > arr [i+1]):
                c = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = c
                swapped= True
        print(arr)
        if(not swapped):
            break
    return arr


'''
    Insertion sort algorithm

'''

def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(arr)
 

'''
    Selection sort algorithm

'''       
    
def selection_sort(arr):
    
    for i in range(len(arr)):
        min_indx = i
        #print(min_indx)
        for j in range(i+1, len(arr)):
            if arr[min_indx] > arr[j]:
                min_indx = j
        arr[i],arr[min_indx] = arr[min_indx] , arr[i]
     
    print(arr)
    return arr


'''
    Merge sort algorithm

'''
def merge_sort(arr,l,r):
    
    if l<r:
        m = (l+(r-1))//2
        print(l,r,m)
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        print('...............')
        merge(arr,l,m,r)
        
def merge(arr,l,m,r):
    print(l,m,r)
    n1 = m-l + 1
    n2 = r-m
    
    L = [0]*n1
    R = [0]*n2 
    
    for i in range(0,n1):
        L[i] = arr[l+1]
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
        
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
        
        
arr = [60,50,5,30,20,10]

sorted_arr = merge_sort(arr,0,len(arr)-1) 
print(sorted_arr)


'''
    Quick sort algorithm

'''

def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)


def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 

print(arr)