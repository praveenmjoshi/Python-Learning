# -*- coding: utf-8 -*-


def linear_serach(arr, item):
    
    for index,value in enumerate(arr):
        print('iter',index)
        if value == item:
            return index
        
    return -1

def binary_search(arr,item):
    
    arr = sorted(arr)
    upper_bound = len(arr)
    lower_bound = 1
    
    index = None
    while(index == None):
        if upper_bound < lower_bound:
            index = -1
            
        mid = int(lower_bound + (upper_bound - lower_bound)/2) 
        print(mid)
        
        if arr[mid] < item:
            lower_bound = mid + 1
            
        if arr[mid] > item:
            upper_bound = mid - 1
            
        if arr[mid] == item:
            index = mid
    
    return index
            

def interpolation_search(arr,item):
    
    arr = sorted(arr)
    upper_bound = len(arr) - 1
    lower_bound = 1
    
    index = None
    while(index == None):
        if upper_bound < lower_bound:
            index = -1
            
        mid = int(lower_bound + ((upper_bound - lower_bound)/ (arr[upper_bound] - arr[lower_bound])) * (item - arr[lower_bound]) ) 
         
        print(mid)
        
        if arr[mid] < item:
            lower_bound = mid + 1
            
        if arr[mid] > item:
            upper_bound = mid - 1
            
        if arr[mid] == item:
            index = mid
    
    return index
    
arr = [10,20,30,40,50,60,70,80,90]

index = linear_serach(arr, 70)
print('index',index)
print('==================')

index = binary_search(arr, 70)
print('index',index)
print('==================')

index = interpolation_search(arr, 70)
print('index',index)