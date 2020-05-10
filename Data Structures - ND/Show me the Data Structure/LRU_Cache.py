#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:12:14 2020

@author: anunay.aatipamula
"""
from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.lru_cache = OrderedDict()
        self.capacity = capacity
        

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.lru_cache.keys():
            value = self.lru_cache.pop(key)
            self.lru_cache[key] = value
            return value
        else:
            return -1
        
    def size(self):
        return len(self.lru_cache)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.capacity <= 0:
            return False
        if key in self.lru_cache.keys():
            self.lru_cache[key] = value
        else:
            if len(self.lru_cache) >= self.capacity:
                self.lru_cache.popitem(last = False)
                self.lru_cache[key] = value
            else:
                self.lru_cache[key] = value
        return True
   
    def __repr__(self):
        return str(self.lru_cache)
        
                
    
#Test Case 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print('Pass' if our_cache.get(1)==1 else 'Fail')
print('Pass' if our_cache.get(2)==2 else 'Fail')
print('Pass' if our_cache.get(9)==-1 else 'Fail')      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)
#[(4, 4), (1, 1), (2, 2), (5, 5), (6, 6)]
our_cache.get(3)
print(our_cache)
print('Pass' if our_cache.get(3)==-1 else 'Fail')# returns -1 because th


#Test Case 2

our_cache2 = LRU_Cache(0)
our_cache2.set(1, 1);
our_cache2.set(2, 2);
print('Pass' if our_cache2.size()==0 else 'Fail')

#Test case 3

our_cache3 = LRU_Cache(-2)
our_cache3.set(1,1)
our_cache3.set(2,2)

print("Pass" if(our_cache3.get(2)==-1) else 'Fail')
print("Pass" if(our_cache3.size()==0) else 'Fail')



     