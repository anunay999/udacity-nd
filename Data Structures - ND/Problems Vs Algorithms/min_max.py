#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 02:00:54 2020

@author: anunay.aatipamula
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if(len(ints)< 1):
        return None
        
    min_val,max_val = ints[0],ints[0]
    for num in ints:
        if min_val > num:
            min_val  =  num
        if max_val  < num:
            max_val = num
    return (min_val,max_val)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if (None == get_min_max([])) else "Fail")
print ("Pass" if ((-1, -1) == get_min_max([-1,-1,-1,-1])) else "Fail")
print ("Pass" if ((-1, 9) == get_min_max([3,-1,0,6,2,9])) else "Fail")
print ("Pass" if ((-1, 4) == get_min_max([3,3,2,2,4,4,-1])) else "Fail")
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
