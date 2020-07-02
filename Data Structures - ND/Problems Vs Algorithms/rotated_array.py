#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:25:14 2020

@author: anunay.aatipamula
"""
from collections import OrderedDict

def rotated_array_search(input_list, number):
    
    input_list = list(OrderedDict.fromkeys(input_list))
    low = 0
    high = len(input_list) - 1

    while low <= high:
        mid = (low + high)//2
        
        if number == input_list[mid]:
            return mid
        
        if input_list[mid] < input_list[high]:
            if number > input_list[mid] and number <= input_list[high]:
                low = mid + 1
            else:
                high = mid - 1
                
        elif input_list[mid] >= input_list[low]:
            if number < input_list[mid] and number >= input_list[low]:
                high = mid - 1
            else:
                low = mid + 1
    return -1   

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    #print(rotated_array_search(input_list, number))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[], 6])
test_function([[1,2,3,4,5,6], 1])
test_function([[1,2,2,2,6], 2])
test_function([[1,1,1,1,1,1], 1])


test_function([[6, 7, 8, 1, 2, 3, 4], 2])
test_function([[6, 7, 8, 1, 2, 3, 4], 3])
test_function([[6, 7, 8, 1, 2, 3, 4], 4])
test_function([[2, 3, 4, 5, 6, 7, 8, 1], 1])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])