#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 01:11:41 2020

@author: anunay.aatipamula
"""

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    
    zero_ind = 0
    two_ind = len(input_list) - 1
    cur_ind = 0

    while cur_ind <= two_ind:
        
        if input_list[cur_ind] == 0:
            input_list[cur_ind],input_list[zero_ind] = input_list[zero_ind],0
            zero_ind += 1
            cur_ind += 1
            
        elif input_list[cur_ind] == 2:           
            input_list[cur_ind],input_list[two_ind] = input_list[two_ind], 2
            two_ind -= 1
        else:
            cur_ind += 1
        #print(input_list)   
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    #print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])