#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 03:00:23 2020

@author: anunay.aatipamula
"""
import math

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return -1
    
    cur_val = number//2
    
    while cur_val < number:
        sqr = cur_val ** 2
        next_sqr = (cur_val+1) ** 2
        #print(sqr,cur_val,next_sqr)
        if sqr == number or (sqr < number and next_sqr > number):
            return cur_val
        elif sqr > number:
            cur_val //=2
        else:
            cur_val +=  1
            
    return cur_val
    
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (-1 == sqrt(-27)) else "Fail")
print ("Pass" if  (4567 == sqrt(20857489)) else "Fail")
print ("Pass" if  (9510 == sqrt(90440100)) else "Fail")