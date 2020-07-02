#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 02:15:52 2020

@author: anunay.aatipamula
"""
def partition(arr,low,high): 
    i = low-1  
    pivot = arr[high]
    for j in range(low , high): 
      if   arr[j] < pivot: 
          i = i+1 
          arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
def quick_sort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quick_sort(arr, low, pi-1) 
        quick_sort(arr, pi+1, high)
    return arr
        
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if(len(input_list)<1):
        return  [-1,-1]
    sorted_list = quick_sort(input_list,0,len(input_list)-1)
    first_num,second_num = str(),str()
    for ind in range(len(sorted_list)-1,-1,-1):
        if len(first_num)>len(second_num):
            second_num+= str(sorted_list[ind])
        else:
            first_num += str(sorted_list[ind])
    #print([int(first_num),int(second_num)])
    return [int(first_num),int(second_num)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[0,0,0,0,0], [0, 0]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[4, 6, 2, 5, 9, 8, 7, 1], [9752, 8641]])
test_function([[3, 0, 4, 6, 2, 5, 9, 8, 7, 1], [97531, 86420]])
test_function([[], [-1, -1]])

